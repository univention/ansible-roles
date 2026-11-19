### Configure tier model

This role applies an Active Directory style tier model (Tier 0 / Tier 1 / Tier 2) to a UCS domain **without Samba/AD**.
Background, test results and the limits of this approach are documented in [docs/tier-model-on-ucs.md](../../docs/tier-model-on-ucs.md).

**Warning:** Delegative administration is an *experimental* UCS 5.2 feature ("Don't use it in production yet"). Try this role in a test environment first.

| Tier | What | Administrators | Delegated rights |
|---|---|---|---|
| 0 | Domain controllers (primary, backup, replica), users, groups, policies | `Domain Admins` | `domain-administrator` (everything) |
| 1 | Member servers | `Tier1 Admins` | modify/remove `computers/memberserver` objects, nothing else |
| 2 | Clients and standard users | `Tier2 Admins` | modify/remove client objects, reset passwords of users in `cn=standard,cn=users` |

The role does the following:

1. Creates the groups `Tier1 Admins` and `Tier2 Admins` and the container for standard users (Primary Directory Node).
2. Installs `/etc/custom-udm-roles.policy`, creates the custom roles `tier1-server-admin` and `tier2-workstation-admin` and assigns the roles to the tier groups via `guardianMemberRoles` (Primary and Backup Directory Node).
3. Creates UMC policies for the tier groups and authorizes the groups for the UDM REST API.
4. Enables delegative administration for UMC and the UDM REST API (only after the roles exist, so `Domain Admins` can not lock themselves out).
5. Restricts logon on every host to the administrators of the host's tier (`auth/<service>/restrict`, `auth/<service>/group/<group>`). `root` stays allowed.
6. If a Samba AD DC is part of the play: creates the tier OUs (`Tier0`, `Tier1`, `Tier2` with sub OUs), delegates computer management (Tier 1/2) and password reset (Tier 2) with AD ACLs, and creates authentication policies/silos with a TGT lifetime per tier for the current tier admins (on the Samba DC with the PDC emulator role).

Hosts are assigned to a tier automatically (domain controllers -> 0, member servers -> 1, everything else -> 2) or via `configure_tier_model_host_tier`.

Users are **not** created by the role. Add the administrator accounts to the tier groups, e.g.:

```bash
udm groups/group modify --dn "cn=Tier1 Admins,cn=groups,$(ucr get ldap/base)" \
  --append users="uid=alice-t1,cn=users,$(ucr get ldap/base)"
```

#### Requirements

- UCS 5.2-2 or newer with the latest errata
- For the Samba part: a domain functional level with authentication silo support (2012 R2 or newer, e.g. via `configure_samba_functional_level`) and the Samba DC with the PDC emulator role in the play
- Run the role against **all** UCS systems of the domain in one play, including the Primary Directory Node. Delegative administration is only configured on Primary and Backup Directory Nodes; the other nodes only get the logon restrictions.
- univention.ucs_modules
  - univention_config_registry
  - univention_directory_manager

#### Role Variables

- `configure_tier_model_tier0_group`(string): Tier 0 admin group; default `Domain Admins`
- `configure_tier_model_tier1_group`(string): Tier 1 admin group, created by the role; default `Tier1 Admins`
- `configure_tier_model_tier2_group`(string): Tier 2 admin group, created by the role; default `Tier2 Admins`
- `configure_tier_model_tier2_user_container`(string): Container relative to the LDAP base with the standard users the Tier 2 helpdesk may support; default `cn=standard,cn=users`
- `configure_tier_model_tier1_computer_types`(list): UDM types managed by Tier 1; default `["computers/memberserver"]`
- `configure_tier_model_tier2_computer_types`(list): UDM types managed by Tier 2; default linux, ubuntu, macos, windows, ipmanagedclient
- `configure_tier_model_host_tier`(string/int): Tier of the host: `auto`, `0`, `1` or `2`; default `auto`
- `configure_tier_model_auth_services`(list): PAM services restricted by UCR; default `login, sshd, other, rlogin, screen, ppp`
- `configure_tier_model_allow_higher_tier_logon`(bool): Allow admins of a more privileged tier to log on to lower tier hosts (breaks the model); default `false`
- `configure_tier_model_enable_delegative_administration`(bool): Configure delegative administration; default `true`
- `configure_tier_model_allow_computer_create`(bool): Let Tier 1/2 create computer objects. **Unsafe**, allows privilege escalation to Tier 0 via the primary group, see the document; default `false`
- `configure_tier_model_enable_samba`(bool): Apply the tier model in Samba/AD if a Samba DC is in the play; default `true`
- `configure_tier_model_samba_tiers`(list): Tier OUs, sub OUs, group and TGT lifetime (minutes) per tier
- `configure_tier_model_samba_computer_aces` / `configure_tier_model_samba_user_support_aces`(list): SDDL ACEs (`{sid}` = tier group SID) set on the tier OUs
- `configure_tier_model_samba_auth_policies`(bool): Create authentication policies/silos; default `true`
- `configure_tier_model_tier1_umc_operations` / `configure_tier_model_tier2_umc_operations`(list): UMC operation sets for the tier groups

#### Dependencies

none

#### Example Playbook

```yaml
---
- name: "Apply the tier model"
  hosts: "all"
  roles:
    - role: "configure_tier_model"
```

Set the tier of a host in the inventory, e.g. a replica node that should be Tier 1: `configure_tier_model_host_tier: 1`.
Note that a writable Samba DC holds all AD secrets and is Tier 0 in the Microsoft model, see the document.

#### License

GNU General Public License v3.0

#### Author Information

Univention GmbH
www.univention.com

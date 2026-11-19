### Configure Samba functional level

This role raises the Samba/AD domain and forest functional level from 2008 R2 to 2016 on a UCS domain.
It follows the procedure from [How to: Samba raise domain functional level to 2016](https://help.univention.com/t/how-to-samba-raise-domain-functional-level-to-2016/24110).

**Warning:** A schema upgrade and a functional level raise cannot be undone by a downgrade. Take current backups of all domain controllers and test the recovery procedure before running this role. Some environments with level 2016 report time synchronization problems between Windows clients and Samba AD DCs, see the article for details.

The role does the following:

1. Checks the prerequisites:
   - `samba-tool` and the package `univention-samba4` are installed on every host.
   - The SchemaMaster and InfrastructureMaster FSMO roles are held by the same server (see `samba-tool fsmo show`) and that server is part of the play.
2. Skips everything if domain level, forest level and lowest DC level are already 2016.
3. Allows schema updates (`samba4/schema/update/allowed`) on the SchemaMaster.
4. Sets the DC functional level (`samba/global/options/ad dc functional level`, `samba4/function/level`) on every DC and restarts Samba there.
5. Upgrades the AD schema to 2019 on the SchemaMaster if `objectVersion` is lower than 88.
6. Runs `samba-tool domain functionalprep` and `samba-tool domain level raise` on the SchemaMaster.
7. Verifies the levels (`samba-tool domain level show`, `msDS-Behavior-Version` = 7), disables schema updates again and restarts Samba on the SchemaMaster.

#### Requirements

- univention.ucs_modules
  - univention_config_registry
- **Run the role against all Samba/AD domain controllers of the domain in the same play.** Every DC must run a Samba version that supports level 2016.

#### Role Variables

- `configure_samba_functional_level_target`(string): Target functional level, only `2016` is supported; default `2016`
- `configure_samba_functional_level_schema_object_version`(int): Minimum schema `objectVersion` before the schema upgrade is skipped; default `88`
- `configure_samba_functional_level_restart_samba`(bool): Restart Samba after changing the DC level; default `true`

#### Dependencies

none

#### Example Playbook

```yaml
---
- name: "Raise Samba functional level to 2016"
  hosts: "samba_dcs"
  roles:
    - role: "configure_samba_functional_level"
```

#### Further reading

- [How to: Samba raise domain functional level to 2016](https://help.univention.com/t/how-to-samba-raise-domain-functional-level-to-2016/24110)

#### License

GNU General Public License v3.0

#### Author Information

Univention GmbH
www.univention.com

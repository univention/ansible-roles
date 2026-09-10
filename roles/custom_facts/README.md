### Custom facts

This role gathers release & ucr information and stores them in `/etc/ansible/facts.d/` on the remote system, making them available via the `ansible_local` namespace.

#### Requirements

none

#### Role Variables

- `custom_facts_templates`(list): filename(s) of templates which should be applied; default: `["deployment.fact.j2", "hotfixes.fact.j2"]`

#### Dependencies

none

#### Example Playbook

```yaml
---
- name: "Gather custom facts"
  hosts: "all"
  roles:
    - role: "custom_facts"
```

After this, you can access the custom facts via the `ansible_local.` namespace, like so:

```yaml
---
- hosts: "all"
  tasks:
    - name: "Install htop on primary"
      pkg:
        - htop
      when: ansible_local.server/role="domaincontroller_master"
```

(This can be done better by limiting the task to the primary node in the inventory, but as an example it's fine)

#### License

GNU General Public License v3.0

#### Author Information

Univention GmbH
<www.univention.com>

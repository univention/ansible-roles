### Workaround: Use specific acme tiny version

This role downloads and patches acme-tiny.

#### Requirements

- ansible.posix
  - patch

#### Role Variables

`workaround_acmetiny_upgrade_temp_dir`(map): Ansible temporary dir for workaround files.

#### Dependencies

none

#### Example Playbook

```yaml
---
- name: "Workaround acme-tiny upgrade"
  hosts: "all"
  roles:
    - role: "workaround_acmetiny_upgrade"
      vars:
        workaround_acmetiny_upgrade_temp_dir: "/tmp/acme-workaround"
```

#### License

GNU General Public License v3.0

#### Author Information

Univention GmbH
www.univention.com

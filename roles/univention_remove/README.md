### Remove packages with univention-remove

This role installs packages via `univention-remove` wrapper.

#### Requirements

none

#### Role Variables

- `univention_remove_name`(string): The name of the package to be removed.

#### Dependencies

none

#### Example Playbook

```yaml
---
- name: "Remove package"
  hosts: "all"
  roles:
    - role: "univention_remove"
      vars:
        univention_remove_name: "nano"
```

#### License

GNU General Public License v3.0

#### Author Information

Univention GmbH
www.univention.com

### Get installed univention apps

This role sets a fact with installed univention apps.

#### Requirements

- ansible.utils
  - cli_parse

#### Role Variables

none

#### Dependencies

none

#### Example Playbook

```yaml
---
- name: "Get installed apps"
  hosts: "all"
  roles:
    - role: "get_installed_apps"
```

#### License

GNU General Public License v3.0

#### Author Information

Univention GmbH
www.univention.com

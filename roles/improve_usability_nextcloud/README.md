### Improve usability nextcloud

This role disables some unused functionality like: `contacts`, `spreed`, `mail`, `calendar`.

#### Requirements

none

#### Role Variables

none

#### Dependencies

none

#### Example Playbook

```yaml
---
- name: "Improve Nextcloud usability"
  hosts: "all"
  roles:
    - role: "improve_usability_nextcloud"
```

#### License

GNU General Public License v3.0

#### Author Information

Univention GmbH
www.univention.com

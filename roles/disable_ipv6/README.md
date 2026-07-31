### Disable IPv6

This role disables IPv6 on system via modprobe.

#### Requirements

- ansible.posix
  - sysctl

#### Role Variables

none

#### Dependencies

none

#### Example Playbook

```yaml
---
- name: "Disable IPv6"
  hosts: "all"
  roles:
    - role: "disable_ipv6"
```

#### License

GNU General Public License v3.0

#### Author Information

Univention GmbH
www.univention.com

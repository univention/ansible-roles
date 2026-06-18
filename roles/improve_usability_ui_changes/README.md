Improve usability ui changes.
=========

This role will improve ui.

Requirements
------------

none

Role Variables
--------------

- `improve_usability_ui_changes_basedn`(): The LDAP base domain name.

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Improve UI usability"
  hosts: "all"
  roles:
    - role: "improve_usability_ui_changes"
      vars:
        improve_usability_ui_changes_basedn: "dc=example,dc=com"
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

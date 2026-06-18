Configure Portal Title
=========

This role configures portal title.

Requirements
------------

none

Role Variables
--------------

- `portal_configure_title_basedn`(string): The LDAP base domain name.
- `portal_configure_title_titles`(list): The new portal titles with locale in format like `de_DE "Cool Portal (Univention)"`.

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Configure portal title"
  hosts: "all"
  roles:
    - role: "portal_configure_title"
      vars:
        portal_configure_title_basedn: "dc=example,dc=com"
        portal_configure_title_titles:
          - "en_US \"My Portal (Univention)\""
          - "de_DE \"Mein Portal (Univention)\""
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

Modify UCS certs
=========

Modify exisiting univention certificates.

Requirements
------------

none

Role Variables
--------------

- `modify_ucs_ca_external_domain_name`(string): The external domain name.
- `modify_ucs_ca_external_domain_part`(string): The part of an external domain eventually excluding fist subdomain.
- `modify_ucs_ca_external_domain_prefix`(string): The first subdomain if exists.

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Modify UCS certificates"
  hosts: "all"
  roles:
    - role: "modify_ucs_ca"
      vars:
        modify_ucs_ca_external_domain_name: "portal.example.com"
        modify_ucs_ca_external_domain_part: "example.com"
        modify_ucs_ca_external_domain_prefix: "portal"
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

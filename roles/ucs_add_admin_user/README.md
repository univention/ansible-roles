Add UCS admin user
=========

This role adds an administrative UCS user.

Requirements
------------

none

Role Variables
--------------

- `ucs_add_admin_user_basedn`(string): The LDAP base domain name.
- `ucs_add_admin_user_username`(string): The username for the administrative user.
- `ucs_add_admin_user_firstname`(string): The firstname for the administrative user.
- `ucs_add_admin_user_lastname`(string): The lastname for the administrative user.
- `ucs_add_admin_user_password`(string): The password for the administrative user.
- `ucs_add_admin_user_recoveryemail`(string): The recovery email address for the administrative user.
- `ucs_add_admin_user_attrib_list`(map): A map of attributes & values to set for the administrative user.
- `ucs_add_admin_user_group_list`(list): A list of group names to append the administrative user to.

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Add admin user"
  hosts: "all"
  roles:
    - role: "ucs_add_admin_user"
      vars:
        ucs_add_admin_user_basedn: "dc=example,dc=com"
        ucs_add_admin_user_username: "adminuser"
        ucs_add_admin_user_firstname: "Admin"
        ucs_add_admin_user_lastname: "User"
        ucs_add_admin_user_password: "secret"
        ucs_add_admin_user_recoveryemail: "admin@example.com"
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

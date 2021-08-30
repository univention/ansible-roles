LDAPSearch user
=========

This role adds specific LDAPSearch users.

Requirements
------------

none

Role Variables
--------------

- `ldapsearch_user_basedn`(string): The LDAP base DN.
- `ldapsearch_user_server_type`(string): Which type of UCS server to set up. The possible options are `master`and `backup`. The default is `master`, which also means "standalone". If `backup` is chosen the following variable also has to be set; default: `master`.
- `ldapsearch_user_hide_logging`(boolean): Toggle template logging; default: `true`.
- `ldapsearch_user_list`(list): A list of ldapsearch users to create.
- `ldapsearch_user_list_tenantbased`(list): A list of LDAPSearch users to create.

Dependencies
------------

none

Example Playbook
----------------

### Configure LDAPSearch user

```yaml
- hosts: all
  tasks:
    - ansible.builtin.include_role:
        name: "univention.ucs_roles.ldapsearch_user"
      vars:
        ldapsearch_user_list:
          - username: "ldapsearch_example"
            name: "Name of LDAPSearch user"           # optional; default value from username
            lastname: "Lastname of LDAPSearch user"   # optional; default value from username
            password: "SuperSecretPassword"
        # ...
```

### Configure LDAPSearch user (per tenant)

```yaml
- hosts: all
  tasks:
    - ansible.builtin.include_role:
        name: "univention.ucs_roles.ldapsearch_user"
      vars:
        ldapsearch_user_list_tenantbased:
          - username: "ldapsearch_example"
            name: "Name of LDAPSearch user"                  # optional; default value from username
            lastname: "Lastname of LDAPSearch user"          # optional; default value from username
            password: "SuperSecretPassword"
            tenant_ou: "ou=users,ou=root,ou=0001,ou=tenants" # position in LDAP
        # ...
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

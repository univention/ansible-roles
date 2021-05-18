LDAPSearch user
=========

This role adds specific LDAPSearch users.

Requirements
------------

none

Role Variables
--------------

- `ldapsearch_user_basedn`(string): The LDAP base DN.
- `ldapsearch_user_nextcloud_password`(string): The password for nextcloud LDAPSearch user.
- `ldapsearch_user_ox_password`(string): The password for OX LDAPSearch user.
- `ldapsearch_user_install_apps`(list): A list of applications to install.

Dependencies
------------

none

Example Playbook
----------------


License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

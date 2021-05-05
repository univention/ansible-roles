Update UMC permissions
=========

This role updates UMC permissions.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------

- `umc_permissions_basedn`(string): The LDAP base domain name.
- `umc_permissions_passwordreset_blacklist_groups`(string): The name of LDAP groups which are not allowed to reset their password.

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

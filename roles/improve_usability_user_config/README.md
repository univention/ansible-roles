Improve usability user configuration
=========

This role improves user configuration.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry

Role Variables
--------------

- `improve_usability_user_config_basedn`(string): The LDAP base domain name.
- `improve_usability_user_config_external_hostname`(string): The host name that is used to talk to the system.
- `improve_usability_user_config_install_apps`(list):  A list of applications to install.

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

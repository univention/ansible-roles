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
- `improve_usability_user_config_mailprimaryaddress_required`(bool): Toggles if mailPrimaryAddress should be required; default: `false`.
- `improve_usability_user_config_firstname_required`(bool): Toggles if forename should be required; default: `false`.
- `improve_usability_user_config_wizard_disabled`(string): Toggles the wizard. When set to `Yes`, wizard is enabled; default: `No`.

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

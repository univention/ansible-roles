Configure directory manager
=========

This role configures directory manager settings.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry
    
Role Variables
--------------

- `configure_directory_manager_mailprimaryaddress_required`(bool): Toggles if mailPrimaryAddress should be required; default: `false`.
- `configure_directory_manager_firstname_required`(bool): Toggles if forename should be required; default: `false`.
- `configure_directory_manager_wizard_disabled`(string): Toggles the wizard. When set to `Yes`, wizard is enabled; default: `No`.

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

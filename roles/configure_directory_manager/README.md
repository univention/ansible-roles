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
- `configure_directory_manager_invite_default`(string): Toggles the default invitation behaviour; default: `"True"`.
- `configure_directory_manager_overridepwlength_visible`(string): Toggles wether the password length override is visible; default: `"False"`.
- `configure_directory_manager_overridepwlength_default`(string): Sets default value for password length override; default: `"False"`.
- `configure_directory_manager_pwdchangenextlogin_visible`(string): Toggles wether password change on next login is visible; default: `"False"`.
- `configure_directory_manager_pwdchangenextlogin_default`(string): Sets default value for password change on next login; default: `"True"`.
- `configure_directory_manager_autosearch`(string): Toggles wether the user autosearch is enabled; default: `"False"`.
- `configure_directory_manager_username_syntax`(string): Set the username syntax; default `"uid"`.

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

Configure SAML single server
=========

This role configures SAML single server.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry

Role Variables
--------------

- `configure_saml_single_server_external_hostname`(string): The hostname that is used to talk to the system.
- `configure_saml_single_server_internal_hostname`(string): The internally used hostname; default `"{{ inventory_hostname }}"`.
- `configure_saml_single_server_external`(bool): Toggle if SAML auth should be configured for external use; default `false`.
- `configure_saml_single_admin_user_name`(string): The UCS administrator's user name, defaults to "Administrator". This variable only is used when joining a backup server. Changing this will NOT change the UCS admin user name, it will only break the backup join scenario.
- `configure_saml_single_temp_file`(map): Tempfile object where univention app password is stored.
- `configure_saml_single_server_type`(string): Which type of UCS server to set up. The possible options are `master`and `backup`. If `backup` is chosen the following variable also has to be set; default: `"master"`.
- `configure_saml_single_server_use_workaround_external_idp_server`(bool): When set to `true` the IDP schema is downloaded from local and not resolved via external hostname; default: `true`.
- `configure_saml_single_server_basedn`(string): The LDAP base dn.
- `configure_saml_single_server_remove_default_saml_provider`(bool): When set to `true` all builtin SAML provider will be removed; default: `true`.

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

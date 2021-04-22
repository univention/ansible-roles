Configure SAML single server
=========

This role configures SAML single server.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry

Role Variables
--------------

- `configure_saml_single_server_external_hostname`(string): The host name that is used to talk to the system.
- `configure_saml_single_admin_user_name`(string): The UCS administrator's user name, defaults to "Administrator". This variable only is used when joining a backup server. Changing this will NOT change the UCS admin user name, it will only break the backup join scenario.
- `configure_saml_single_temp_file`(map): Tempfile object where univention app password is stored.

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
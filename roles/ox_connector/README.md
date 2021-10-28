OX Connector
=========

This role configures and install OX connector.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `ox_connector_basedn`(string): The LDAP base dn.
- `ox_connector_domain_name`(string): The system's dns domain name.
- `ox_connector_domain_prefix`(string): The system's dns domain prefix. Useful when OX server is in same network
- `ox_connector_soap_prefix`(string): The ox soap server prefix; default: `ox-provisioning`.
- `ox_connector_app_version_map`(map): A dictionary that maps application names to specific versions that ought to be installed.
- `ox_connector_temp_pw_file`(map): Tempfile object where univention app password is stored.
- `ox_connector_master_admin`(string): The name of OX administrator.
- `ox_connector_master_password`(string): The password of OX administrator.
- `ox_connector_server_type`(string): Which type of UCS server to set up. The possible options are `master`and `backup`. The default is `master`, which also means "standalone". If `backup` is chosen the following variable also has to be set; default: `master`.
- `ox_connector_template_name`(string): The name of default template; default: `"standard"`.
- `ox_connector_ox_drive_default`(number): Toggles OXDrive state; default: `0`.
- `ox_connector_hide_logging`(boolean): Toggle logging of sensitive information like password; default: `true`.

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

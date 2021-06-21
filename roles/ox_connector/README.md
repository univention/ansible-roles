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
- `ox_connector_app_version_map`(map): A dictionary that maps application names to specific versions that ought to be installed. 
- `ox_connector_temp_pw_file`(map): Tempfile object where univention app password is stored.
- `ox_connector_soap_server_name`(string): The DNS name of OX SOAP server.
- `ox_connector_soap_server_ip`(string): The IP address of OX SOAP server.
- `ox_connector_master_admin`(string): The name of OX administrator.
- `ox_connector_master_password`(string): The password of OX administrator.
- `ox_connector_server_type`(string): Which type of UCS server to set up. The possible options are `master`and `backup`. The default is `master`, which also means "standalone". If `backup` is chosen the following variable also has to be set; default: `master`.

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

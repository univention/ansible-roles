DC Connector
=========

This role configures and install Dovecot (DC) connector.

Requirements
------------

none

Role Variables
--------------

- `ox_connector_basedn`(string): The LDAP base dn.
- `ox_connector_domain_name`(string): The system's dns domain name.
- `ox_connector_domain_prefix`(string): The system's dns domain prefix. Useful when dovecot server is in same network.
- `ox_connector_soap_prefix`(string): The ox soap server prefix; default: `ox-provisioning`.
- `ox_connector_server_type`(string): Which type of UCS server to set up. The possible options are `master`and `backup`.
The default is `master`, which also means "standalone".
If `backup` is chosen the following variable also has to be set; default: `master`.


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

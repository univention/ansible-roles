Print a deployment message
=========

This role prints information about playbook, its dependencies and configuration.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `deployment_message_verification_pause_duration`(number): 20
- `deployment_message_external_hostname`(string): the host name that is used to talk to the system
- `deployment_message_domain_name`(string): the system's dns domain name
- `deployment_message_basedn`(string): the LDAP base domain name
- `deployment_message_server_type`(string): type of UCS server to set up. The possible options are `master`and `backup`.
- `deployment_message_saml_config_type`(string): can be set to "failover" or basically anything else. In "failover" mode a part of the SAML configuration is omitted. "failover" in this case refers to a UCS native SAML failover mode. Any other value will result in the same configuration being deployed, the value therefore is more of a descriptive nature. Recommended values are "loadbalancer", "primary-secondary" or "standalone" with the latter being the default value.

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

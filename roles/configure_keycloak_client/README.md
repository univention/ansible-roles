Configure keycloak client
=========

This role configures ucs to properly use keycloak.

Requirements
------------

none

Role Variables
--------------

- `configure_keycloak_client_oidc_broker_secret`(string): The client password used in the IDP creation.
- `configure_keycloak_client_keycloak_password`(string): The keycloaks password.
- `configure_keycloak_client_basedn`(string): The LDAP base domain name.
- `configure_keycloak_client_keycloak_server_id`(string): The OpenID Connect IDP broker ID. This is used in both config modes.
- `configure_keycloak_client_keycloak_server`(string): The server the UCS system with authenticate against.
- `configure_keycloak_client_config_type`(string): This variable determines if the keycloak server configuration is done using this role (`dynamic`) or if things already have been configured and only the UCS side has to be configured (`static`). `dynamic` usually is used for setups with a lot of turnover, `static` is used in a more static environment. If set to 'none' keycloak configuration as a whole will be skipped, including the "client" side; default: `dynamic`.
- `configure_keycloak_client_hostname`(string): The systems hostname; default: `"{{ inventory_hostname }}"`

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

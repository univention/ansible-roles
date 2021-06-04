Configure Keycloak
=========

This role configures keycloak, either via KCADM or REST.

Requirements
------------

none

Role Variables
--------------

- `configure_keycloak_generate_oidc_broker_secret`(bool): If set to true the client password used in the IDP creation is generated dynamically. If it is set to `false` the value in `configure_keycloak_oidc_broker_secret` is used instead. If `configure_keycloak_config_type` is set to `static` this variable implicitly is set to `false`; default: `true`
- `configure_keycloak_oidc_broker_secret`(string): Client password used in the IDP creation. Only used when `configure_keycloak_generate_oidc_broker_secret`is set to false.
- `configure_keycloak_oidcidp_id`(string): The name of the OpenID Connect Identity Provider to be configured when using `dynamic` configuration; default: `"{{ inventory_hostname }}"`.
- `configure_keycloak_server_id`(string): The OpenID Connect IDP broker ID. This is used in both config modes and defaults to `keycloak`.
- `configure_keycloak_oidc_username_template`(string): default: `"${CLAIM.preferred_username}_${ALIAS}"` 
- `configure_keycloak_client_callback_url`(string): When configuring a new client on the keycloak server this URL is used as the OpenID callback URL. Defaults to none but has to be set IF the client doesn't exist already. If it does this variable is not used as the client is not going to be updated.
- `configure_keycloak_config_method`(string): The configuration method against keycloak, either `kcadm` or `rest`; default: `kcadm`
- `configure_keycloak_config_type`(string): This variable determines if the keycloak server configuration is done using this role (`dynamic`) or if things already have been configured and only the UCS side has to be configured (`static`). `dynamic` usually is used for setups with a lot of turnover, `static` is used in a more static environment. If set to 'none' keycloak configuration as a whole will be skipped, including the "client" side; default: `dynamic`.
- `configure_keycloak_keycloak_server`(string): The server the UCS system with authenticate against.
- `configure_keycloak_auth_realm`(string): As the name says, the realm that is used to authenticate our keycloak operations against. This is not the realm used for client configuration, for that the host's domain is used; default: `master`.
- `configure_keycloak_admin_username`(string): The username used to authenticate to keycloak server when configuring the authentication connection, best stored in a secrets manager or encrypted using ansible-vault. 
- `configure_keycloak_admin_password`(string): The password used to authenticate to keycloak server when configuring the authentication connection, best stored in a secrets manager or encrypted using ansible-vault
- `configure_keycloak_realm`(string): default: `"{{ hostvars[inventory_hostname]['ansible_domain'] }}"`
- `configre_keycloak_fqdn`(string): default: `"{{ hostvars[inventory_hostname]['ansible_fqdn'] }}"`
- `configure_keycloak_client_id`(string): The client's client id used to authenticate.
- `configure_keycloak_display_matrix_in_iframe`(bool): When set to 'true', the hosts FQDN is added to CSP list. Be careful, the corresponding field has a size limit; default: `false`.
- `configure_keycloak_client_secret`(string): default: `false`
- `configure_keycloak_base_url`(string): default: `"https://{{ configure_keycloak_keycloak_server }}/auth"`
- `configure_keycloak_realm_base_url`(string): default: `"{{ configure_keycloak_base_url }}/admin/realms/{{ ansible_domain }}"`
- `configure_keycloak_protocol_mapper_name`(string): default: `"identity-provider-mapper"`
- `configure_keycloak_import_mapper_name`(string): default: `"append IDP to username"`
- `configure_keycloak_hostname`(string): The systems hostname; default: `"{{ inventory_hostname }}"`

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

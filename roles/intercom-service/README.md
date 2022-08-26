Intercom Service
=========

This role installs and comfigures the intercom service.
For further information have a look at https://docs.software-univention.de/intercom-service/latest/index.html

Requirements
------------

none

Role Variables
--------------

- `intercom_service_hide_logging`(boolean): Toggle template logging; default: `true`.
- `intercom_service_domain_name`(string): The domain name. default: `""`
- `intercom_service_temp_pw_file`: The tmp file within the administrator password.
- `intercom_service_settings_proxy`(string): Wether to allow connections via proxy server instead of backend directly; default: `"False"`
- `intercom_service_settings_client_id`(string): The keycloak client ID; default: `intercom`
- `intercom_service_settings_intercom_url`(string): URL where ICS is reachable; default: `https://ics.{{ intercom_service_domain_name }}`
- `intercom_service_settings_base_url`(string): Base URL used to identify with the IdP; default: `https://ics.{{ intercom_service_domain_name }}`
- `intercom_service_settings_origin_regex`(string): Defines the origin CORS regex; default: `{{ intercom_service_domain_name }}`
- `intercom_service_keycloak_url`(string): URL of the Keycloak instance to be used as the IdP; default: `https://id.{{ intercom_service_domain_name }}`
- `intercom_service_keycloak_realm_name`(string): Name of the realm containing the configured OIDC Intercom client; default: `ucs`
- `intercom_service_matrix_url`(string): The URL on which the Matrix server is reachable default: `https://matrix.{{ intercom_service_domain_name }}`
- `intercom_service_matrix_server_name`(string): The server name of the matrix server; default: `https://matrix.{{ intercom_service_domain_name }}`
- `intercom_service_matrix_login_type`(string): The login-type ICS should use on the matrix server; default: `uk.half-shot.msc2778.login.application_service`
- `intercom_service_matrix_nordeck_mode`(string): The connection mode of the Nordeck-bot; default: `test`
- `intercom_service_nordeck_url`(string): The URL on which Nordeck-bot is listening; default: `https://meetings-widget-bot.{{ intercom_service_domain_name }}`
- `intercom_service_portal_url`(string): The URL on which the Univention-Portal is listening; default: `https://portal.{{ intercom_service_domain_name }}`
- `intercom_service_ox_origin`(string): The OX CORS origin setting; default: `https://webmail.{{ intercom_service_domain_name }}`
- `intercom_service_ox_audience`(string): The OIDC audience settings for the OX token request send to the IdP; default: `oxoidc`
- `intercom_service_nc_url`(string): The URL on which Nextcloud is listening on; default: `https://fs.{{ intercom_service_domain_name }}`
- `intercom_service_nc_origin`(string): The Nextcloud CORS origin; default: `https://fs.{{ intercom_service_domain_name }}`

Dependencies
------------

none

Example Playbook
----------------

## Intercom Service

```yaml
- hosts: all
  tasks:
    - name: "Install Intercom Service via Appcenter"
      ansible.builtin.include_role:
        name: "univention.ucs_roles.intercom_service"
      vars:
        intercom_service_hide_logging: false
        intercom_service_domain_name: "ucs.test.intranet"
        intercom_service_temp_pw_file: "{{ temp_file }}"
        intercom_service_keycloak_realm_name: "your_keycloak_realm"

```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

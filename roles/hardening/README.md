Hardening system
=========

This role reduces security risks by disabling default settings, like root login.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------

- `hardening_disable_http`(bool): If set to `true`, `http` will be disabled in apache2. Only `https` will be available; default: `true`
- `hardening_hsts`(bool): If set to `true` HTTP Strict Transport Security is enabled for apache2 ; default: `true`
- `hardening_apache2_ssl_tlsv13`(bool): If set to `true` ssl tlsv11 and tlsv12 are disabled for apache2; default: `true`
- `hardening_apache2_server_tokens`(string): Set apache2 configuration to `Prod`, `Major`, `Minor`, `Min`, `OS`or `Full`. Details: https://httpd.apache.org/docs/2.4/mod/core.html#servertokens ; default: `Prod`
- `hardening_apache2_server_signature`(string): Set apache2 configuration to `Off` , `EMail` or `On`. Details: https://httpd.apache.org/docs/2.4/mod/core.html#serversignature ; default: `Off`
- `hardening_honorcipherorder`(string): During the negotiation of cryptographic algorithms during the setup of a SSL/TLS connection the preference of the client is used by default. If this option is enabled, the preference of the server is used instead. The list of algorithms offered by Apache can be configured with the variable 'apache2/ssl/ciphersuite'; default: `true`
- `hardening_ciphersuite`(string): his configures the cryptopgraphic algorithms which are offered to clients during a SSL handshake. The format is described at <http://httpd.apache.org/docs/2.4/mod/mod_ssl.html#sslciphersuite>; default: `HIGH`
- `hardening_umc_session_cookie`(bool): If set to `true` the login cookie is a session cookie. Closing the browser will delete the cookie, effectively logging out the user; default: `true`
- `hardening_umc_secure_cookie`(bool): If set, cookies are set with the secure attribute if the connection is using HTTPS; default: `true`
- `hardening_umc_cookie_samesite`(string): Set the SameSite cookie attribute for UMC cookies. Possible values: `Strict`, `Lax` and `None`; default: `Strict`
- `hardening_saml_idp_language_cookie_samesite`(string): Set the SameSite attribute in sthe language cookie attribute of SAML IDP. Possible values: `Strict`, `Lax` and `None`; default: `Strict`
- `hardening_saml_idp_session_cookie_samesite`(string): Set the "SameSite" attribute in the session cookie of SAML IDP. Possible values: `Strict`, `Lax` and `None`; default: `Strict`
- `hardening_saml_idp_session_cookie`(bool): If set to `true` the "Secure" attribute in the session cookie is activated. default: `true`
- `hardening_saml_idp_language_cookie`(bool): If set to `true` the "Secure" attribute in the language cookie is activated. default: `true`
- `hardening_disable_umc_http_tracebacks`(bool): If set to `true` tracebacks are no longer shown to the user in error case for umc; default: `true`
- `hardening_disable_udm_rest_tracebacks`(bool): If set to `true` tracebacks are no longer shown to the user in ror case for udm REST; default: `true`
- `hardening_disable_saml_idp_errors`(bool): If set to `true` tracebacks are no longer shown to the user in error case for the saml idp; default: `true`
- `hardening_disable_saml_idp_error_reporting`(bool): If set to `true` error information and stack traces can not be reported via email to the technical contact mail address; default: `true`


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

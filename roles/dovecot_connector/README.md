DC Connector
=========

This role configures and install Dovecot (DC) connector.

Requirements
------------

none

Role Variables
--------------

- `dovecot_connector_basedn`(string): The LDAP base dn.
- `dovecot_connector_domain_name`(string): The system's dns domain name.
- `dovecot_connector_domain_prefix`(string): The system's dns domain prefix. Useful when dovecot server is in same network.
- `dovecot_connector_soap_prefix`(string): The ox soap server prefix; default: `ox-provisioning`.
- `dovecot_connector_server_type`(string): Which type of UCS server to set up. The possible options are `master` and `backup`.
The default is `master`, which also means "standalone".
If `backup` is chosen the following variable also has to be set; default: `master`.
- `dovecot_connector_app_version_map`(map): A dictionary that maps application names to specific version of dovecot connector. default: `""`
- `dovecot_connector_temp_pw_file`: The tmp file within the administrator password.
- `dovecot_connector_adm_accepted_exit_codes`(string): DoveAdm-exitCode-Werte, die nicht zum Abbruch führen; default: `68 75`
- `dovecot_connector_adm_host`(string): Der Domänenname des Servers auf dem DoveAdm aktiviert wurde; default: `dc-provisioning.dovecot_connector_domain_name`
- `dovecot_connector_adm_port`(string): Der Port auf dem DoveAdm erreichbar ist; default: `443`
- `dovecot_connector_adm_username`(string): Benutzername des DoveAdm; default: `""`
- `dovecot_connector_adm_password`(string): Passwort des DoveAdm; default: `""`
- `dovecot_connector_adm_uri`(string): DoveAdm URL Vorlage. Mögliche Variablen `{dcc_adm_host}` und `{dcc_adm_port}`; default: `https://{dcc_adm_host}:{dcc_adm_port:d}/doveadm/v1`
- `dovecot_connector_dc_vmail_template`(string): Das vmail Verzeichnis welches Dovecot nutzt. Mögliche Variablen `{uuid}`, `{email}`, `{domain}` und `{username}`; default: `/data/usr/local/dovecot/vmail/{uuid[0]}{uuid[1]}/{uuid}`
- `dovecot_connector_loglevel`(string): Die Log-Stufe der Anwendung. Werte: `DEBUG`, `INFO`, `WARNING` und `ERROR`; default: `INFO`
- `dovecot_connector_hide_logging`(bool): Toggle logging output; default: `true`

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

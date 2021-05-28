Configure Postfix (apps)
=========

This role modifies postfix configuration.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------

- `configure_apps_postfix_domain_name`(string): The system's dns domain name.
- `configure_apps_postfix_external_hostname`(string): The host name that is used to talk to the system.
- `configure_apps_postfix_relay_port`(number): The port that is used to talk to the system; default: `25`.
- `configure_apps_postfix_use_relay_host`(bool): Toggles if a SMTP relay host should be used; default: `false`.
- `configure_apps_postfix_relay_host`(string): The SMTP relay hostname.
- `configure_apps_postfix_relay_username`(string): The SMTP relay username.
- `configure_apps_postfix_relay_password`(string): The SMTP relay password.

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

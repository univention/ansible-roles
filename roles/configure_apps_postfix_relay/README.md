Configure Postfix relay (apps)
=========

This role modifies postfix relay configuration.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `configure_apps_postfix_relay_enabled`(bool): Toggles if a SMTP relay host should be used; default: `false`.
- `configure_apps_postfix_relay_port`(number): The port that is used to talk to the system; default: `25`.
- `configure_apps_postfix_relay_host`(string): The SMTP relay hostname.
- `configure_apps_postfix_relay_username`(string): The SMTP relay username.
- `configure_apps_postfix_relay_password`(string): The SMTP relay password.
- `configure_apps_postfix_relay_hide_logging`(boolean): Toggles output logging for sensible information; default: `true`.

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

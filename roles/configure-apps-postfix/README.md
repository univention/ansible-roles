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
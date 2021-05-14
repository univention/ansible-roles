Pre installation steps of OpenXchange (OX)
=========

This role prepares OX installation.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `install_apps_ox_pre_external_hostname`(string): The host name that is used to talk to the system.
- `install_apps_ox_pre_mail_domain`(string): The externally managed mail domain.
- `install_apps_ox_pre_basedn`(string): The LDAP base domain name.

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

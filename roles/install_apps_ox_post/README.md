Post installation steps of OpenXchange (OX)
=========

This role configures OX.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry
- community.crypto
  - openssl_pkcs12
- community.general
  - java_cert    

Role Variables
--------------

- `install_apps_ox_post_basedn`(string): The LDAP base domain name.
- `install_apps_ox_post_external_hostname`(string): The host name that is used to talk to the system.
- `install_apps_ox_post_ox_keystore_passphrase`(string): The passphrase for ox keystore.
- `install_apps_ox_post_ox_drive_default`(string): Toggle OXDrive by setting `0`for disabled and `1` for enabled; default: `0`.

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

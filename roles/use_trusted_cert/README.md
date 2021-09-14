Use trusted SSL certificate
=========

This role configures an issues SSL certificate from trusted authorities.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry


Role Variables
--------------

- `use_trusted_cert_path_cert`(string): Local path to SSL (chained) certificate file.
- `use_trusted_cert_path_key`(string): Local path to SSL key file.

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

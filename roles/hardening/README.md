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

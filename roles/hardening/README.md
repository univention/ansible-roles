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
- `hardening_apache2_server_tokens`(string): Set apache2 configuration to `Prod`, `Major`, `Minor`, `Min`, `OS`or `Full`. Details: https://httpd.apache.org/docs/2.4/mod/core.html#servertokens ; default: `Prod`
- `hardening_apache2_server_signature`(string): Set apache2 configuration to `Off` , `EMail` or `On`. Details: https://httpd.apache.org/docs/2.4/mod/core.html#serversignature ; default: `Off`

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

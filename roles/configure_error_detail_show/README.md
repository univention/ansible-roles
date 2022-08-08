Configure error detail show
=========

This role configures if the error messages will display the details.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------

- `configure_error_detail_show_http_tracebacks`(bool): Defines whether tracebacks are shown to the user in error cases; default: `false`
- `configure_error_detail_show_directory_manager_rest_tracebacks`(bool): Defines whether tracebacks are shown to the user in error cases; default: `false`
- `configure_error_detail_show_saml_idp_errors`(bool): Defines if error information and stack traces allowed to be shown to the user; default: `false`
- `configure_error_detail_show_saml_idp_error_reporting`(bool): Defines if error information and stack traces can be reported via email to the technical contact mail address; default: `false`

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

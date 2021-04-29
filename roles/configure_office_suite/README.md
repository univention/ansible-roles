Configure office suite
=========

This role configures the chosen office suite and installs it.

Requirements
------------

none

Role Variables
--------------

- `configure_office_suite_office_suite`(string): Define the to be installed office suite. Defaults to `collabora-online`. A list of supported suites is defined in `configure_office_suite_supported_office_suites`; default: `"collabora-online"`.
- `configure_office_suite_supported_office_suites`(list): A list of supported office suites that can be installed using this role. This variable is set in the role's `defaults/main.yml` and should not be changed.
- `configure_office_suite_onlyoffice_formats`(map): A map of onlyoffice file formats to be enabled or disabled.
- `configure_office_suite_collabora_license_key`(string): Include a valid license for collabora-online.
- `configure_office_suite_app_version_map`(map): A dictionary that maps application names to specific versions that ought to be installed.
- `configure_office_suite_temp_pw_file`(map): Tempfile object where univention app password is stored.
- `configure_office_suite_install_apps`(list): A list of applications to install.

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
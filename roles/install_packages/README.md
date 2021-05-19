Install packages
=========

This role installs univention apps with/without fixed versions.

Requirements
------------

none

Role Variables
--------------

- `install_packages_app_version_map`(map): A dictionary that maps application names to specific versions that ought to be installed. See also `install_packages_force_package_upgrade` for a way to upgrade already installed software.
- `install_packages_service_name_list`(list): A list containing application names to be installed.
- `install_packages_temp_pw_file`(map): Tempfile object where univention app password is stored.
- `install_packages_force_package_upgrade`(bool): If set to true already installed application versions are checked and if the installed version differs from what has been specified in `install_packages_app_version_map` that version is installed instead. Choosing `false` results in the role ignoring already installed software and skip installation; default: `false`.
- `install_packages_install_apps`(list): A list of applications to install.
- `install_packages_additional_options`(string): Additional option that could be set during install.

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

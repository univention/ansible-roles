Install new portal (service)
=========

This role installs and configures new portal.

Requirements
------------

none

Role Variables
--------------

- `install_service_new_portal_service_version_map`(map): A dictionary that maps service names to specific versions that ought to be installed. See also `install_service_new_portal_force_package_upgrade` for a way to upgrade already installed software.
- `install_service_new_portal_force_package_upgrade`(bool): If set to true already installed application versions are checked and if the installed version differs from what has been specified in `install_service_new_portal_service_version_map` that version is installed instead. Choosing `false` results in the role ignoring already installed software and skip installation; default: `false`.
- `install_service_new_portal_temp_file`(map): Ansible temporary dir.

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

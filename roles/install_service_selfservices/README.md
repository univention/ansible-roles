Install selfservices service
=========

This role installs selfservice services.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------

- `install_service_selfservice_service_version_map`(map): A dictionary that maps service names to specific versions that ought to be installed. See also `install_service_selfservice_force_package_upgrade` for a way to upgrade already installed software.
- `install_service_selfservice_temp_file`(map): Ansible temporary dir.
- `install_service_selfservice_force_package_upgrade`(bool): If set to true already installed application versions are checked and if the installed version differs from what has been specified in `install_service_selfservice_service_version_map` that version is installed instead. Choosing `false` results in the role ignoring already installed software and skip installation; default: `false`.
- `install_service_selfservice_external_hostname`(string): The host name that is used to talk to the system.
- `install_service_selfservice_install_services`(list): A list of services to install.
- `install_service_selfservice_domain_name`(string): The LDAP base domain name.
- `install_service_selfservice_password_reset_filename`(string): The name of password reset template.

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

Install letsencrypt
=========

This role installs letsencrypt and configures it. It supports letsencrypt staging as well.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry

Role Variables
--------------

- `install_lets_encrypt_use_letsencrypt_staging`(bool): When `false` it uses regular let's encrypt certificates, `true` switches to the staging area for testing purposes; default: `false`.
- `install_lets_encrypt_implement_ugly_letsencrypt_workaround`(bool): Work around bugs in the let's encrypt staging implementation. This patches files in the univention letsencrypt app; default: `false`.
- `install_lets_encrypt_temp_pw_file`(map): Ansible temporary password file.
- `install_lets_encrypt_temp_dir`(map): Ansible temporary dir.
- `install_lets_encrypt_service_version_map`(map): A dictionary that maps service names to specific versions that ought to be installed. See also `install_packages_force_package_upgrade` for a way to upgrade already installed software.
- `install_lets_encrypt_service_name_list`(list): A list containing service names to be installed.  
- `install_lets_encrypt_force_package_upgrade`(bool): If set to true already installed application versions are checked and if the installed version differs from what has been specified in `install_lets_encrypt_service_version_map` that version is installed instead. Choosing `false` results in the role ignoring already installed software and skip installation; default: `false`.
- `install_lets_encrypt_external_hostname`(string): The host name that is used to talk to the system.

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
Upgrade Univention UCS
=========

This role upgrade UCS to a specific version.

Requirements
------------

none

Role Variables
--------------

- `univention_upgrade_version`(string): The UCS' version number to upgrade to; default: `"4.4-99"`.
- `univention_upgrade_clear_apt_cache`(bool): Clear all downloaded packages to reduce package conflicts; default: `false`.
- `univention_upgrade_removal_check`(bool): Check if packages will be removed during upgrade; default: `false`.
- `univention_upgrade_reboot_after_upgrade`(bool): Reboot UCS after package upgrade; default: `false`.
- `univention_upgrade_app_updates`(bool): Upgrade apps during univention-upgrade; default: `false`.
- `univention_upgrade_username`(string): Username of administrative user for app updates; default: `Administrator`.
- `univention_upgrade_password_file`(string): Path to the file on the server that contains the user password if `univention_upgrade_app_updates=true`; default: `""`.

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

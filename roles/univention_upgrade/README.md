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

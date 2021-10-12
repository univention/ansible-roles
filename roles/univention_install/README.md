Install packages with univention-install
=========

This role installs packages via `univention-install` wrapper.

Requirements
------------

none

Role Variables
--------------

- `univention_install_name`(string): The name of the package to be installed.
- `univention_install_clear_apt_cache`(bool): Clear all downloaded packages to reduce package conflicts; default: `false`.

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

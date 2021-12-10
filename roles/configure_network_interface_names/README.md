Configure network interface names
=========

This role configures network interface names as GRUB boot parameter, resulting in network interface names like eth0.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `configure_network_interface_names_use_old_names`(boolean): Set the GRUB parameter for old interface names; default: `true`.

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

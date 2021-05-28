UMC maintenance policies
=========

This role sets UMC maintenance policies.

Requirements
------------

none

Role Variables
--------------

- `umc_policies_maintenance_basedn`(string): The LDAP base domain name.
- `umc_policies_maintenance_patchhour`(string): The chosen hour for univention-update; default: `5`.
- `umc_policies_maintenance_patchminute`(string): The choosen minute for univention-update; default: `00`.
- `umc_policies_maintenance_patchday`(String): The chosen day for univention-update; default: `Tuesday`.
- `umc_policies_maintenance_release_verion`(string): The univention release version.

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

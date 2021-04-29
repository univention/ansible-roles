Create portal entry
=========

This role creates a new portal entry.

Requirements
------------

none

Role Variables
--------------

- `portal_create_entry_base_dn`(string): The base DN that has been used when setting up the UCS server
- `portal_create_entry_entries`(map): The portal entries map.
- `portal_create_entry_install_list`(list): Combine apps/services/customization lists.
- `portal_create_entry_member_attribute_map`(map): The member attributes.
- `portal_create_entry_entry_map`(map): The portal entry entries.

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
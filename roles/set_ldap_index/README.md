Configure LDAP Index
=========

This role adds/removes additional ldap indexes. Slapd.service is stopped. Run this role only in maintenance.
Without extra vars nothing will happen.

Requirements
------------

none

Role Variables
--------------

- `set_ldap_index_equality_add`(string): The name of the ldap attribute for equality searches to add; default: ""
- `set_ldap_index_presence_add`(string): The name of the ldap attribute for presence searches to add; default: ""
- `set_ldap_index_approx_add`(string): The name of the ldap attribute for approx searches to add; default: ""
- `set_ldap_index_substring_add`(string): The name of the ldap attribute for substring searches to add; default: ""
- `set_ldap_index_equality_rm`(string): The name of the ldap attribute for equality searches to remove; default: ""
- `set_ldap_index_presence_rm`(string): The name of the ldap attribute for presence searches to remove; default: ""
- `set_ldap_index_approx_rm`(string): The name of the ldap attribute for approx searches to remove; default: ""
- `set_ldap_index_substring_rm`(string): The name of the ldap attribute for substring searches to remove; default: ""

Dependencies
------------

none

Example Playbook
----------------

- hosts: ucs_master
  become: true
  tasks:
    - name: "include role for setting ldap index"
      ansible.builtin.include_role:
        name: "roles/set_ldap_index"
      vars:
        set_ldap_index_equality_add: "isOxUser"
        set_ldap_index_approx_rm "aAAARecord"


License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

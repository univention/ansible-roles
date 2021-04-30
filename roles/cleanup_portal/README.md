Cleanup Portal
=========

Remove default and unused portal entries.

Requirements
------------

none

Role Variables
--------------

- `cleanup_portal_basedn`(string): The LDAP base domain name.
- `cleanup_portal_install_services`(list): A list of services to install.
- `cleanup_portal_domain_admin_group`(string): default: `"cn=Domain Admins,cn=groups,{{ cleanup_portal_basedn }}"`.
- `cleanup_portal_portal_dn`(string): default: `"cn=portals,cn=univention,{{ cleanup_portal_basedn }}"`.
- `cleanup_portal_prometheus_dn`(string): default: `'cn=prometheus,cn=entry,{{ cleanup_portal_portal_dn }}'`.
- `cleanup_portal_admin_dashboard_dn`(string): default: `'cn=admin-dashboard,cn=entry,{{ cleanup_portal_portal_dn }}'`.

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

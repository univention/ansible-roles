Install multitenant ACLs
=========

Install and configure ACL package.

Requirements
------------

none

Role Variables
--------------

- `install_multitenant_acls_customer_name`(string): The name of customer used inside ACL package.
- `install_multitenant_acls_multitenant_acls`(list): A list of acl settings.
    ```
    multitenant_acls:
      - tenant_id: "0000"
        admin_password: ""
      - tenant_id: "0001"
        admin_password: ""
      - tenant_id: "0002"
        tenant_short_name: "test"
        admin_password: ""
        mail_domains: []
    ```
- `install_multitenant_acls_json_path`(string): The local path for ACL structure json file.
- `install_multitenant_acls_package_name`(string): The customer specific debian package name.
- `install_multitenant_acls_script_name`(string): The name of create acl structure script.
- `install_multitenant_acls_keycloak_base`(string): The base url for keycloak.

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

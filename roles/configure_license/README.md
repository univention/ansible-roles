Configure UCS license
=========

This role helps to apply an existing license file or claims a new license from shop.

Requirements
------------

none

File Structure
--------------

```text
files/
 |
 +-- license_client.py
```

Role Variables
--------------

- `configure_license_validity`(string): The validity period for the license in a format GNU date is able to understand as a time period, like "12 weeks".
- `configure_license_shop_password`(string): The shop user's password, best stored in a secrets manager or encrypted via ansible-vault.
- `configure_license_shop_id`(number): Which license shop to use when obtaining a new license for the server.
- `configure_license_shop_username`(string): The shop's user name, needed for authentication.
- `configure_license_max_users`(number): How many users to allow on the server.
- `configure_license_basedn`(string): The LDAP base domain name.
- `configure_license_type`(string): Choose one of `local_license` or `server_license`. When choosing `local_license` a license file name has to be provided otherwise choose `server_license` and one is generated; default: `server_license`.
- `configure_license_file`(string): If `configure_license_type` set to `local_license` then provide license file name here; default: `false`.
- `configure_license_server_type`(string): Which type of UCS server to set up. The possible options are `master`and `backup`. The default is `master`, which also means "standalone". If `backup` is chosen the following variable also has to be set; default: `master`.

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

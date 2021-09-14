Install branding package
=========

This role installs a customer branding package.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `install_branding_customer_repo_name`(string): The name of customer debian repository.
- `install_branding_customer_repo_parts`(string): The part of customer debian repository.
- `install_branding_customer_repo_password`(string): The password of customer debian repository.
- `install_branding_customer_repo_server`(string): The server of customer debian repository.
- `install_branding_customer_repo_username`(string): The username of customer debian repository.
- `install_branding_customer_branding_package`(string): Set the name of the Debian Branding Package in the Univention Customer Repository.

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

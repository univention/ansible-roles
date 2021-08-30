Configure repository
=========

Configure repository URLs to use own apt repository server.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `configure_repository_default_repository_prefix`(string): Define access method, either `"http://"` or `"https://"`; default: `"https://"`.
- `configure_repository_default_repository_server`(string): The repository server without any prefix or suffix or path.
- `configure_repository_default_repository_path`(string): The repository path/suffix where repository could be found on server.
- `configure_repository_default_repository_username`(string): Optionally configure username for authentication.
- `configure_repository_default_repository_password`(string): Optionally configure password for authentication.

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

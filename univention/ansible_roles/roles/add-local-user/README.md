Add local user
=========

This role creates a local user and allows login.

Requirements
------------

- univention_config_registry

Role Variables
--------------

- `add_local_user_user`(map): A map containing user information:
```
add_local_user_user:
    name:         # username; default; "ansible"
    comment:      # user comment; default: "ansible user"
    password:     # hased password of user; default:  "{{ "ansible"|password_hash('sha512') }}"
    sshkey_file:  # ssh key filename; default: empty
    sshkey:       # ssh key as string; default: empty
```
- `add_local_user_default_shell`(string): Default user shell; default: `/bin/bash`

Dependencies
------------

none

Example Playbook
----------------


License
-------

BSD

Author Information
------------------

Univention GmbH
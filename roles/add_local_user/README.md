Add local user
=========

This role creates a local user with ssh login permissions.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry

Role Variables
--------------

- `add_local_user_user`(map): A map containing user information:

```
add_local_user_user:
    name:         # username; default; "ansible"
    comment:      # user comment; default: "ansible user"
    password:     # hashed password of user; default:  "{{ 'ansible'|password_hash('sha512') }}"
    sshkey_file:  # ssh key filename; default: empty
    sshkey:       # ssh key as string; default: empty
    state:        # toggle if user should be present or absent; default: present
```

- `add_local_user_default_shell`(string): Default user shell; default: `/bin/bash`
- `add_local_user_default_password_policy`(string): Default password update policy.
  Possible values are `"on_create"` and `"always"`; default `"on_create"`.
- `add_local_user_system_user`(bool): `true` if the user should be a system user instead of a human; default: `true`.

Dependencies
------------

`passlib`

Example Playbook
----------------

```yaml
---
- name: "Add a testuser"
  hosts: "all"
  roles:
    - role: "add_local_user"
      vars:
        add_local_user_user_name: "testuser"
        add_local_user_user_comment: "For testing the add_local_user_user role"
        add_local_user_user_password: "{{ 'univention' | password_hash('sha512') }}"
        add_local_user_user_state: "present"
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

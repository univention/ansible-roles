Update users SSH keys
=========

This role adds and removes SSH keys from user.

Requirements
------------

- ansible.posix
  - authorized_key

File Structure
--------------

```text
files/
 |
 +-- ssh_keys/
 |   |
 |   +-- add/
 |   |   |
 |   |   +-- *.pubkey
 |   |
 |   +-- remove/
 |       |
 |       +-- *.pubkey
```

Role Variables
--------------

- `update_users_ssh_keys_user`(string): Name of local user where SSH keys should be added/removed.

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Update SSH keys"
  hosts: "all"
  roles:
    - role: "update_users_ssh_keys"
      vars:
        update_users_ssh_keys_user: "root"
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

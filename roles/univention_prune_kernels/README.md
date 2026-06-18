Prune Kernels Univention UCS
=========

This role prunes kernels for UCS servers in order to free space at /boot.

Requirements
------------

none

Role Variables
--------------

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Prune old kernels"
  hosts: "all"
  roles:
    - role: "univention_prune_kernels"
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

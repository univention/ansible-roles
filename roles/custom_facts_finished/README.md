Custom facts (finished)
=========

Store rollout finished information in custom facts directory.

Requirements
------------

none

Role Variables
--------------

none

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Mark deployment finished"
  hosts: "all"
  roles:
    - role: "custom_facts_finished"
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

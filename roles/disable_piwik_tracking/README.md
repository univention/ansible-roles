Toogle piwik tracking
=========

This role enables/disables piwik tracking of UCS.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `disable_piwik_tracking_disable`(bool): Toggles piwik tracking of installation. When set to `true`, tracking is disabled; default: `true`.

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Disable Piwik tracking"
  hosts: "all"
  roles:
    - role: "disable_piwik_tracking"
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

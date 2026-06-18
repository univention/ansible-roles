Set feedback mail address
=========


Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------
- `set_feedback_mail_address_web_feedback_mail`(string): Email address configured to send the traceback if occurs an error in the Univention Management Console; default: `feedback@univention.de`


Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Set feedback mail address"
  hosts: "all"
  roles:
    - role: "set_feedback_mail_address"
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

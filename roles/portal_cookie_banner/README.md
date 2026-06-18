Toggle portal cookie banner
=========

This roles enables/disables a cookie banner in portal frontend.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `portal_configure_title_basedn`(string): The base DN that has been used when setting up the UCS server
- `portal_configure_title_titles`(list): The cookie banner title and body.
```
portal_configure_title_titles:
  de:
    title: "We are using cookies"
    text: ""
```

Dependencies
------------

none

Example Playbook
----------------

```yaml
---
- name: "Configure cookie banner"
  hosts: "all"
  roles:
    - role: "portal_cookie_banner"
      vars:
        portal_cookie_banner_data:
          de:
            title: "Wir verwenden Cookies"
            text: "Diese Website verwendet Cookies."
          en:
            title: "We are using cookies"
            text: "This website uses cookies."
```

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

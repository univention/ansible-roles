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


License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

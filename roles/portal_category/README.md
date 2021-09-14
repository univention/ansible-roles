Portal category
=========

Create, modify and delete portal categories

Requirements
------------

none

Role Variables
--------------

- `portal_category_base_dn`(string): The base DN that has been used when setting up the UCS server
- `portal_category_categories`(list): The portal categories list.
- `portal_category_install_list`(list): Combined apps/services/customization lists.
- `portal_category_drift_detection`(bool): Toggle drift detection and only apply differences; default: `true`.
- `portal_category_remove_unscoped`(bool): Toggle removal of undefined categories; default: `false`.

Dependencies
------------

none

Example Playbook
----------------

```yaml
- hosts: all
  tasks:
    - ansible.builtin.include_role:
        name: "univention.ucs_roles.portal_category"
      vars:
        portal_category_base_dn: "dc=ansible,dc=univention,dc=de"
        portal_category_install_list: ["nextcloud"]
        portal_category_drift_detection: true
        portal_category_remove_unscoped: false
        portal_category_categories:
          - name: "domain-service"
            display_name:
              de_DE: "Applikationen"
              en_US: "Applications"
            state: "present"
            parent: "domain"
          - name: "domain-admin"
            display_name:
              de_DE: "Verwaltung"
              en_US: "Administration"
            state: "present"
            parent: "domain"
          - name: "local-admin"
            display_name:
              de_DE: "Verwaltung"
              en_US: "Administration"
            state: "present"
            parent: "local"
          # ...
```

Portal categories
----------------

```yaml
portal_category_categories:
  - name:           # (string, required) | Name of portal category.
    display_name:   # (map)              | I18n name displayed in portal.
      de_DE:        # (string)           | F.e. german translation.
      en_US:        # (string)           | F.e. english translation.
    only:           # (string)           | Modify when app defined is in `portal_category_install_list`.
    parent:         # (string)           | The name of portal where the category should be appended to, f.e. "domain".
    state:          # (string, required) | State of entry, should be "present" or "absent".
```


Limitations
----------------

- Modifying/Removing attributes with whitespaces are not supported by UCS 4.4

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

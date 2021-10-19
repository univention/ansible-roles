Portal entry
=========

Create, modify, delete and append portal entries.

Requirements
------------

none

Role Variables
--------------

- `portal_entry_base_dn`(string): The base DN that has been used when setting up the UCS server
- `portal_entry_entries`(list): The portal entries list.
- `portal_entry_install_list`(list): Combined apps/services/customization lists.
- `portal_entry_drift_detection`(bool): Toggle drift detection and only apply differences; default: `true`.
- `portal_entry_remove_unscoped`(bool): Toggle removal of undefined entries; default: `false`.

Dependencies
------------

none

Example Playbook
----------------

### Create a public login and file store

```yaml
- hosts: all
  tasks:
    - ansible.builtin.include_role:
        name: "univention.ucs_roles.portal_entry"
      vars:
        portal_entry_base_dn: "dc=ansible,dc=univention,dc=de"
        portal_entry_install_list: ["nextcloud"]
        portal_entry_drift_detection: true
        portal_entry_remove_unscoped: false
        portal_entry_entries:
          - name: "Anmeldung"
            anonymous: true
            category: "help"
            description:
              de_DE: "Anmelden"
              en_US: "Login"
            display_name:
              de_DE: "Anmelden"
              en_US: "Login"
            icon_file: "ucs_portal_login_icon.svg"
            link:
              de_DE: "/univention/saml/?location=%2Funivention%2Fportal%2F"
              en_US: "/univention/saml/?location=%2Funivention%2Fportal%2F"
            linktarget: "samewindow"
            parent: "category"
            state: "present"
            type: "entries"
          - name: "Dateien"
            activated: true
            allowed_groups: ["cn=Domain Users,cn=groups,dc=ansible,dc=univention,dc=de"]
            anonymous: false
            category: "Kollaboration"
            description:
              de_DE: "Dateienablage und -austausch"
              en_US: "File storage and exchange"
            display_name:
              de_DE: "Eigene Dateien"
              en_US: "My files"
            icon_file: "ucs_portal_files_icon.svg"
            linktarget: "newwindow"
            link:
              de_DE: "/nextcloud"
              en_US: "/nextcloud"
            only: "nextcloud"
            parent: "category"
            state: "present"
            type: "entries"
          # ...
```

Portal entries
----------------

```yaml
portal_entry_entries:
  - name:           # (string, required) | Name of portal entry.
    activated:      # (boolean)          | Enable/Disable portal entry.
    allowed_groups: # (list)             | A list of LDAP groups the entry should be shown.
    anonymous:      # (boolean)          | Show entry for not logged-in user.
    category:       # (string)           | Name of category/portal the entry should be appended.
    description:    # (map)              | I18n description displayed in portal.
      de_DE:        # (string)           | F.e. german translation.
      en_US:        # (string)           | F.e. english translation.
    display_name:   # (map)              | I18n name displayed in portal.
      de_DE:        # (string)           | F.e. german translation.
      en_US:        # (string)           | F.e. english translation.
    icon_file:      # (string)           | Name of predefined images or local images.
    link:           # (map)              | Internal or external link.
      de_DE:        # (string)           | F.e. german translation.
      en_US:        # (string)           | F.e. english translation.
    linktarget:     # (string)           | Link target f.e. "samewindow", "newwindow", "embedded" or "useportaldefault".
    only:           # (string)           | Modify when app defined is in `portal_entry_install_list`.
    parent:         # (string)           | The type where entry should be appended, f.e. "category" or "portal".
    state:          # (string, required) | State of entry, should be "present" or "absent".
    type:           # (string)           | The list from parent where entry should be appended. For
                    #                    |  - "category" > possible: "entries"
                    #                    |  - "portal" > possible: "menuLinks", "userLinks"
```

Limitations
----------------

- Modifying/Removing attributes with whitespaces are not supported by UCS 4.4
- Drift detection does not detect changes in icons.

License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

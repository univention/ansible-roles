### Configure Keycloak SAML

This role configures Keycloak as SAML provider.

#### Requirements

none

#### Role Variables

- `configure_keycloak_saml_basedn`(string): The LDAP base dn.
- `configure_keycloak_saml_sp_base_url`(string): The Service Provider base url.

#### Dependencies

none

#### Example Playbook

```yaml
---
- name: "Configure Keycloak SAML"
  hosts: "all"
  roles:
    - role: "configure_keycloak_saml"
      vars:
        configure_keycloak_saml_basedn: "dc=example,dc=com"
        configure_keycloak_saml_sp_base_url: "https://sp.example.com"
```

#### License

GNU General Public License v3.0

#### Author Information

Univention GmbH
www.univention.com

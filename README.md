# UCS Ansible Roles 

This repository only contains ansible roles usable in an ansible-playbook to install and bootstrap UCS.

# Modules

- [hardening](#roleshardeningreadmemd)
- [configure_keycloak](#rolesconfigure_keycloakreadmemd)
- [umc_permissions](#rolesumc_permissionsreadmemd)
- [configure_license](#rolesconfigure_licensereadmemd)
- [extend_root_lvm_volume](#rolesextend_root_lvm_volumereadmemd)
- [remove_packages](#rolesremove_packagesreadmemd)
- [install_service_new_portal](#rolesinstall_service_new_portalreadmemd)
- [workaround_high_mtu](#rolesworkaround_high_mtureadmemd)
- [custom_facts](#rolescustom_factsreadmemd)
- [disable_ipv6](#rolesdisable_ipv6readmemd)
- [ucs_join](#rolesucs_joinreadmemd)
- [portal_deactivate_entry](#rolesportal_deactivate_entryreadmemd)
- [install_branding](#rolesinstall_brandingreadmemd)
- [force_package_list_update](#rolesforce_package_list_updatereadmemd)
- [portal_delete_category](#rolesportal_delete_categoryreadmemd)
- [install_apps_ox_pre](#rolesinstall_apps_ox_prereadmemd)
- [univention_upgrade](#rolesunivention_upgradereadmemd)
- [update_users_ssh_keys](#rolesupdate_users_ssh_keysreadmemd)
- [configure_office_suite](#rolesconfigure_office_suitereadmemd)
- [ox_connector](#rolesox_connectorreadmemd)
- [install_service_selfservices](#rolesinstall_service_selfservicesreadmemd)
- [configure_saml_single_server](#rolesconfigure_saml_single_serverreadmemd)
- [configure_keycloak_client](#rolesconfigure_keycloak_clientreadmemd)
- [deployment_message](#rolesdeployment_messagereadmemd)
- [umc_policies_maintenance](#rolesumc_policies_maintenancereadmemd)
- [portal_configure_title](#rolesportal_configure_titlereadmemd)
- [improve_usability_ui_changes](#rolesimprove_usability_ui_changesreadmemd)
- [configure_apps_postfix](#rolesconfigure_apps_postfixreadmemd)
- [configure_keycloak_saml](#rolesconfigure_keycloak_samlreadmemd)
- [improve_usability_user_config](#rolesimprove_usability_user_configreadmemd)
- [set_dns_glue_record](#rolesset_dns_glue_recordreadmemd)
- [ucs_add_admin_user](#rolesucs_add_admin_userreadmemd)
- [portal_deactivate_category](#rolesportal_deactivate_categoryreadmemd)
- [install_lets_encrypt](#rolesinstall_lets_encryptreadmemd)
- [cleanup_portal](#rolescleanup_portalreadmemd)
- [portal_create_entry](#rolesportal_create_entryreadmemd)
- [configure_apps_owncloud](#rolesconfigure_apps_owncloudreadmemd)
- [get_installed_apps](#rolesget_installed_appsreadmemd)
- [portal_delete_entry](#rolesportal_delete_entryreadmemd)
- [configure_nextcloud_saml](#rolesconfigure_nextcloud_samlreadmemd)
- [install_apps_ox_post](#rolesinstall_apps_ox_postreadmemd)
- [portal_create_category](#rolesportal_create_categoryreadmemd)
- [install_packages](#rolesinstall_packagesreadmemd)
- [add_local_user](#rolesadd_local_userreadmemd)
- [univention_firewall](#rolesunivention_firewallreadmemd)
- [configure_apps_nextcloud](#rolesconfigure_apps_nextcloudreadmemd)
- [disable_piwik_tracking](#rolesdisable_piwik_trackingreadmemd)
- [install_univention](#rolesinstall_univentionreadmemd)
- [configure_ntp_servers](#rolesconfigure_ntp_serversreadmemd)
- [workaround_acmetiny_upgrade](#rolesworkaround_acmetiny_upgradereadmemd)
- [improve_usability_nextcloud](#rolesimprove_usability_nextcloudreadmemd)
- [ldapsearch_user](#rolesldapsearch_userreadmemd)

---

# roles/hardening/README.md

Hardening system
=========

This role reduces security risks by disabling default settings, like root login.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------

- `hardening_disable_http`(bool): If set to `true`, `http` will be disabled in apache2. Only `https` will be available; default: `true`

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

---

# roles/configure_keycloak/README.md

Configure Keycloak
=========

This role configures keycloak, either via KCADM or REST.

Requirements
------------

none

Role Variables
--------------

- `configure_keycloak_generate_oidc_broker_secret`(bool): If set to true the client password used in the IDP creation is generated dynamically. If it is set to `false` the value in `configure_keycloak_oidc_broker_secret` is used instead. If `configure_keycloak_config_type` is set to `static` this variable implicitly is set to `false`; default: `true`
- `configure_keycloak_oidc_broker_secret`(string): Client password used in the IDP creation. Only used when `configure_keycloak_generate_oidc_broker_secret`is set to false.
- `configure_keycloak_oidcidp_id`(string): The name of the OpenID Connect Identity Provider to be configured when using `dynamic` configuration; default: `"{{ inventory_hostname }}"`.
- `configure_keycloak_server_id`(string): The OpenID Connect IDP broker ID. This is used in both config modes and defaults to `keycloak`.
- `configure_keycloak_oidc_username_template`(string): default: `"${CLAIM.preferred_username}_${ALIAS}"` 
- `configure_keycloak_client_callback_url`(string): When configuring a new client on the keycloak server this URL is used as the OpenID callback URL. Defaults to none but has to be set IF the client doesn't exist already. If it does this variable is not used as the client is not going to be updated.
- `configure_keycloak_config_method`(string): The configuration method against keycloak, either `kcadm` or `rest`; default: `kcadm`
- `configure_keycloak_config_type`(string): This variable determines if the keycloak server configuration is done using this role (`dynamic`) or if things already have been configured and only the UCS side has to be configured (`static`). `dynamic` usually is used for setups with a lot of turnover, `static` is used in a more static environment. If set to 'none' keycloak configuration as a whole will be skipped, including the "client" side; default: `dynamic`.
- `configure_keycloak_keycloak_server`(string): The server the UCS system with authenticate against.
- `configure_keycloak_auth_realm`(string): As the name says, the realm that is used to authenticate our keycloak operations against. This is not the realm used for client configuration, for that the host's domain is used; default: `master`.
- `configure_keycloak_admin_username`(string): The username used to authenticate to keycloak server when configuring the authentication connection, best stored in a secrets manager or encrypted using ansible-vault. 
- `configure_keycloak_admin_password`(string): The password used to authenticate to keycloak server when configuring the authentication connection, best stored in a secrets manager or encrypted using ansible-vault
- `configure_keycloak_realm`(string): default: `"{{ hostvars[inventory_hostname]['ansible_domain'] }}"`
- `configre_keycloak_fqdn`(string): default: `"{{ hostvars[inventory_hostname]['ansible_fqdn'] }}"`
- `configure_keycloak_client_id`(string): The client's client id used to authenticate.
- `configure_keycloak_display_matrix_in_iframe`(bool): When set to 'true', the hosts FQDN is added to CSP list. Be careful, the corresponding field has a size limit; default: `false`.
- `configure_keycloak_client_secret`(string): default: `false`
- `configure_keycloak_base_url`(string): default: `"https://{{ configure_keycloak_keycloak_server }}/auth"`
- `configure_keycloak_realm_base_url`(string): default: `"{{ configure_keycloak_base_url }}/admin/realms/{{ ansible_domain }}"`
- `configure_keycloak_protocol_mapper_name`(string): default: `"identity-provider-mapper"`
- `configure_keycloak_import_mapper_name`(string): default: `"append IDP to username"`
- `configure_keycloak_hostname`(string): The systems hostname; default: `"{{ inventory_hostname }}"`

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

---

# roles/umc_permissions/README.md

Update UMC permissions
=========

This role updates UMC permissions.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------

- `umc_permissions_basedn`(string): The LDAP base domain name.
- `umc_permissions_passwordreset_blacklist_groups`(string): The name of LDAP groups which are not allowed to reset their password.

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

---

# roles/configure_license/README.md

Configure UCS license
=========

This role helps to apply an existing license file or claims a new license from shop.

Requirements
------------

none

File Structure
--------------

```text
files/
 |
 +-- license_client.py
```

Role Variables
--------------

- `configure_license_validity`(string): The validity period for the license in a format GNU date is able to understand as a time period, like "12 weeks".
- `configure_license_shop_password`(string): The shop user's password, best stored in a secrets manager or encrypted via ansible-vault.
- `configure_license_shop_id`(number): Which license shop to use when obtaining a new license for the server.
- `configure_license_shop_username`(string): The shop's user name, needed for authentication.
- `configure_license_max_users`(number): How many users to allow on the server.
- `configure_license_basedn`(string): The LDAP base domain name.
- `configure_license_type`(string): Choose one of `local_license` or `server_license`. When choosing `local_license` a license file name has to be provided otherwise choose `server_license` and one is generated; default: `server_license`.
- `configure_license_file`(string): If `configure_license_type` set to `local_license` then provide license file name here; default: `false`.
- `configure_license_server_type`(string): Which type of UCS server to set up. The possible options are `master`and `backup`. The default is `master`, which also means "standalone". If `backup` is chosen the following variable also has to be set; default: `master`.

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


---

# roles/extend_root_lvm_volume/README.md

Extend root LVM volume
=========

Extend the root volume to all available space. Helpful when using a prebuild image and additional space is required.

Requirements
------------

- community.general
  - parted
  - lvg
  - lvol  

Role Variables
--------------

- `extend_root_lvm_volume_extend_lvm_to_whole_disk`(bool): If true, root volume is extended to available space; default: `true`
- `extend_root_lvm_volume_lvm_disk`(string): The "physical" disk to partition without the "/dev/" part, for instance "sda" for "/dev/sda". Defaults to what is used in the Univention QCOW image; default: `"vda"`
- `extend_root_lvm_volume_lvm_vg_name`(string): The volume group the data volume resides in.  Defaults to what is used in the Univention QCOW image; default: `"vg_ucs"`
- `extend_root_lvm_volume_lvm_data_volume`(string): The LVM name used for the data volume. Defaults to what is used in the Univention QCOW image; default: `"root"`
- `extend_root_lvm_volume_existing_lvm_partition_number`(number): The existing lvm partition number. Defaults to what is used in the Univention QCOW image; default: `2`

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

---

# roles/remove_packages/README.md

Remove packages
=========

This role removes univention apps with/without fixed versions.

Requirements
------------

none

Role Variables
--------------

- `remove_packages_app_version_map`(map): A dictionary that maps application names to specific versions that ought to be installed. See also `install_packages_force_package_upgrade` for a way to upgrade already installed software.
- `remove_packages_temp_pw_file`(map): Tempfile object where univention app password is stored.
- `remove_packages_force_package_upgrade`(bool): If set to true already installed application versions are checked and if the installed version differs from what has been specified in `install_packages_app_version_map` that version is installed instead. Choosing `false` results in the role ignoring already installed software and skip installation; default: `false
- `remove_packages_remove_apps`(list): A list of applications to install.
- `remove_packages_app_version_map`(map): A map of packages with/without version to be removed.
- `remove_packages_service_name_list`(list): A list containing application names to be installed.

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

---

# roles/install_service_new_portal/README.md

Install new portal (service)
=========

This role installs and configures new portal.

Requirements
------------

none

Role Variables
--------------

- `install_service_new_portal_service_version_map`(map): A dictionary that maps service names to specific versions that ought to be installed. See also `install_service_new_portal_force_package_upgrade` for a way to upgrade already installed software.
- `install_service_new_portal_force_package_upgrade`(bool): If set to true already installed application versions are checked and if the installed version differs from what has been specified in `install_service_new_portal_service_version_map` that version is installed instead. Choosing `false` results in the role ignoring already installed software and skip installation; default: `false`.
- `install_service_new_portal_temp_file`(map): Ansible temporary dir.

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

---

# roles/workaround_high_mtu/README.md

Workaround: Fix MTU for Docker
=========

When MTU in Docker `1500` is higher than the one for network interface, this
role sets the Docker MTU to `1400`.

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


License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

---

# roles/custom_facts/README.md

Custom facts
=========

This role gathers release information and store them an remote system. 

Requirements
------------

none

Role Variables
--------------

- `custom_facts_templates`(list): filename(s) of templates which should be applied; default: `["deployment.fact.j2", "hotfixes.fact.j2"]`

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

---

# roles/disable_ipv6/README.md

Disable IPv6
=========

This role disables IPv6 on system via modprobe.

Requirements
------------

- ansible.posix
  - sysctl

Role Variables
--------------

none

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

---

# roles/ucs_join/README.md

UCS join
=========

This role runs a UCS Join on master or backup servers.

Requirements
------------

none

Role Variables
--------------

- `ucs_join_derive_root_password_from_hostname`(bool): Creates a unique root/admin password that is derived from the host name, or rather the numeric part of it.
- `ucs_join_derive_root_password_prefix`(string): The prefix that is used before the numeric part in derived passwords.
- `ucs_join_server_type`(string): Which type of UCS server to set up. The possible options are `master`and `backup`. The default is `master`, which also means "standalone". If `backup` is chosen the following variable also has to be set, default: `master`.
- `ucs_join_master_server`(string): In case of a `backup` server (see previous variable) this declares which master server to use. In every other case this variable is ignored.
- `ucs_join_admin_user_name`(string): The UCS administrator's user name, defaults to "Administrator". This variable only is used when joining a backup server. Changing this will NOT change the UCS admin user name, it will only break the backup join scenario.
- `ucs_join_root_password`(string): The machine's root password, if you want version control consider using ansible-vault to encrypt it. If `ucs_join_derive_root_password_from_hostname` is set to true this variables is ignored.
- `ucs_join_hostname`(string): Remote hostname; default `{{ inventory_hostname }}`.
- `ucs_join_domain_name`(string): The system's dns domain name.
- `ucs_join_basedn`(string): The LDAP base domain name.
- `ucs_join_network_config_type`(string): Choose `dhcp` or `static` with the former being the default. If you choose "static" you'll have to add `ucs_join_network_config_static-*` variable as well; default: `dhcp`.
- `ucs_join_network_config_static_ip_config`(map): The server's IPv4 address in one of the following two forms: `<ip address>/<netmask>` or CIDR form (`<ip address>/<prefix length>`. Both forms are functionally equal. Example: `192.168.0.1/255.255.255.240` or `192.168.0.1/28`.
- `ucs_join_network_config_static_dns_servers`(list): A list of DNS servers to use in case of static network configuration. If `ucs_join_server_type` is `backup` this variable is ignored and the `master` server will be used instead.
- `ucs_join_network_config_static_gateway`(string): The server's default router aka internet gateway. This is mandatory for the setup to work.


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

---

# roles/portal_deactivate_entry/README.md

Deactivate portal entry
=========

This role deactivates a portal entry.

Requirements
------------

none

Role Variables
--------------

- `portal_deactivate_entry_base_dn`(string): The base DN that has been used when setting up the UCS server
- `portal_deactivate_entry_entries`(map): The portal entries map.
- `portal_deactivate_entry_install_list`(list): Combine apps/services/customization lists.

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
---

# roles/install_branding/README.md

Install branding package
=========

This role installs a customer branding package.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `install_branding_customer_repo_name`(string): The name of customer debian repository.
- `install_branding_customer_repo_parts`(string): The part of customer debian repository.
- `install_branding_customer_repo_password`(string): The password of customer debian repository.
- `install_branding_customer_repo_server`(string): The server of customer debian repository.
- `install_branding_customer_repo_username`(string): The username of customer debian repository.
- `install_branding_customer_branding_package`(string): Set the name of the Debian Branding Package in the Univention Customer Repository.

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
---

# roles/force_package_list_update/README.md

Force package list update
=========

This role updates univention and apt package lists.

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



License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com
---

# roles/portal_delete_category/README.md

Delete portal category
=========

This role deletes a portal category.

Requirements
------------

none

Role Variables
--------------

- `portal_delete_category_base_dn`(string): The base DN that has been used when setting up the UCS server
- `portal_delete_category_categories`(map): The portal categories map.
- `portal_delete_category_install_list`(list): Combine apps/services/customization lists.

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
---

# roles/install_apps_ox_pre/README.md

Pre installation steps of OpenXchange (OX)
=========

This role prepares OX installation.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `install_apps_ox_pre_external_hostname`(string): The host name that is used to talk to the system.
- `install_apps_ox_pre_mail_domain`(string): The externally managed mail domain.
- `install_apps_ox_pre_basedn`(string): The LDAP base domain name.

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

---

# roles/univention_upgrade/README.md

Upgrade Univention UCS
=========

This role upgrade UCS to a specific version.

Requirements
------------

none

Role Variables
--------------

- `univention_upgrade_version`(string): The UCS' version number to upgrade to; default: `"4.4-99"`.

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

---

# roles/update_users_ssh_keys/README.md

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


License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com
---

# roles/configure_office_suite/README.md

Configure office suite
=========

This role configures the chosen office suite and installs it.

Requirements
------------

none

Role Variables
--------------

- `configure_office_suite_office_suite`(string): Define the to be installed office suite. Defaults to `collabora-online`. A list of supported suites is defined in `configure_office_suite_supported_office_suites`; default: `"collabora-online"`.
- `configure_office_suite_supported_office_suites`(list): A list of supported office suites that can be installed using this role. This variable is set in the role's `defaults/main.yml` and should not be changed.
- `configure_office_suite_onlyoffice_formats`(map): A map of onlyoffice file formats to be enabled or disabled.
- `configure_office_suite_collabora_license_key`(string): Include a valid license for collabora-online.
- `configure_office_suite_app_version_map`(map): A dictionary that maps application names to specific versions that ought to be installed.
- `configure_office_suite_temp_pw_file`(map): Tempfile object where univention app password is stored.
- `configure_office_suite_install_apps`(list): A list of applications to install.

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
---

# roles/ox_connector/README.md

OX Connector
=========

This role configures and install OX connector.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `ox_connector_basedn`(string): The LDAP base dn.
- `ox_connector_app_version_map`(map): A dictionary that maps application names to specific versions that ought to be installed. 
- `ox_connector_temp_pw_file`(map): Tempfile object where univention app password is stored.
- `ox_connector_soap_server_name`(string): The DNS name of OX SOAP server.
- `ox_connector_soap_server_ip`(string): The IP address of OX SOAP server.
- `ox_connector_master_admin`(string): The name of OX administrator.
- `ox_connector_master_password`(string): The password of OX administrator.

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

---

# roles/install_service_selfservices/README.md

Install selfservices service
=========

This role installs selfservice services.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------

- `install_service_selfservice_service_version_map`(map): A dictionary that maps service names to specific versions that ought to be installed. See also `install_service_selfservice_force_package_upgrade` for a way to upgrade already installed software.
- `install_service_selfservice_temp_file`(map): Ansible temporary dir.
- `install_service_selfservice_force_package_upgrade`(bool): If set to true already installed application versions are checked and if the installed version differs from what has been specified in `install_service_selfservice_service_version_map` that version is installed instead. Choosing `false` results in the role ignoring already installed software and skip installation; default: `false`.
- `install_service_selfservice_external_hostname`(string): The host name that is used to talk to the system.
- `install_service_selfservice_install_services`(list): A list of services to install.
- `install_service_selfservice_domain_name`(string): The LDAP base domain name.
- `install_service_selfservice_password_reset_filename`(string): The name of password reset template.

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

---

# roles/configure_saml_single_server/README.md

Configure SAML single server
=========

This role configures SAML single server.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry

Role Variables
--------------

- `configure_saml_single_server_external_hostname`(string): The hostname that is used to talk to the system.
- `configure_saml_single_server_internal_hostname`(string): The internally used hostname; default `"{{ inventory_hostname }}"`.
- `configure_saml_single_server_external`(bool): Toggle if SAML auth should be configured for external use; default `false`.
- `configure_saml_single_admin_user_name`(string): The UCS administrator's user name, defaults to "Administrator". This variable only is used when joining a backup server. Changing this will NOT change the UCS admin user name, it will only break the backup join scenario.
- `configure_saml_single_temp_file`(map): Tempfile object where univention app password is stored.
- `configure_saml_single_server_type`(string): Which type of UCS server to set up. The possible options are `master`and `backup`. If `backup` is chosen the following variable also has to be set; default: `"master"`.
- `configure_saml_single_server_use_workaround_external_idp_server`(bool): When set to `true` the IDP schema is downloaded from local and not resolved via external hostname; default: `true`.
- `configure_saml_single_server_basedn`(string): The LDAP base dn.
- `configure_saml_single_server_remove_default_saml_provider`(bool): When set to `true` all builtin SAML provider will be removed; default: `true`.

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

---

# roles/configure_keycloak_client/README.md

Configure keycloak client
=========

This role configures ucs to properly use keycloak.

Requirements
------------

none

Role Variables
--------------

- `configure_keycloak_client_oidc_broker_secret`(string): The client password used in the IDP creation.
- `configure_keycloak_client_keycloak_password`(string): The keycloaks password.
- `configure_keycloak_client_basedn`(string): The LDAP base domain name.
- `configure_keycloak_client_keycloak_server_id`(string): The OpenID Connect IDP broker ID. This is used in both config modes.
- `configure_keycloak_client_keycloak_server`(string): The server the UCS system with authenticate against.
- `configure_keycloak_client_config_type`(string): This variable determines if the keycloak server configuration is done using this role (`dynamic`) or if things already have been configured and only the UCS side has to be configured (`static`). `dynamic` usually is used for setups with a lot of turnover, `static` is used in a more static environment. If set to 'none' keycloak configuration as a whole will be skipped, including the "client" side; default: `dynamic`.
- `configure_keycloak_client_hostname`(string): The systems hostname; default: `"{{ inventory_hostname }}"`

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

---

# roles/deployment_message/README.md

Print a deployment message
=========

This role prints information about playbook, its dependencies and configuration.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `deployment_message_verification_pause_duration`(number): 20
- `deployment_message_external_hostname`(string): the host name that is used to talk to the system
- `deployment_message_domain_name`(string): the system's dns domain name
- `deployment_message_basedn`(string): the LDAP base domain name
- `deployment_message_server_type`(string): type of UCS server to set up. The possible options are `master`and `backup`.
- `deployment_message_saml_config_type`(string): can be set to "failover" or basically anything else. In "failover" mode a part of the SAML configuration is omitted. "failover" in this case refers to a UCS native SAML failover mode. Any other value will result in the same configuration being deployed, the value therefore is more of a descriptive nature. Recommended values are "loadbalancer", "primary-secondary" or "standalone" with the latter being the default value.

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

---

# roles/umc_policies_maintenance/README.md

UMC maintenance policies
=========

This role sets UMC maintenance policies.

Requirements
------------

none

Role Variables
--------------

- `umc_policies_maintenance_basedn`(string): The LDAP base domain name.
- `umc_policies_maintenance_patchhour`(string): The chosen hour for univention-update; default: `5`.
- `umc_policies_maintenance_patchminute`(string): The choosen minute for univention-update; default: `00`.
- `umc_policies_maintenance_patchday`(String): The chosen day for univention-update; default: `Tuesday`.
- `umc_policies_maintenance_release_verion`(string): The univention release version.
- `umc_policies_maintenance_hostname`(string): The systems hostname; default: `"{{ inventory_hostname }}"`

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

---

# roles/portal_configure_title/README.md

Configure Portal Title
=========

This role configures portal title.

Requirements
------------

none

Role Variables
--------------

- `portal_configure_title_basedn`(string): The LDAP base domain name.
- `portal_configure_title_titles`(list): The new portal titles with locale in format like `de_DE "Cool Portal (Univention)"`.

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

---

# roles/improve_usability_ui_changes/README.md

Improve usability ui changes.
=========

This role will improve ui.

Requirements
------------

none

Role Variables
--------------

- `improve_usability_ui_changes_basedn`(): The LDAP base domain name.

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
---

# roles/configure_apps_postfix/README.md

Configure Postfix (apps)
=========

This role modifies postfix configuration.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------

- `configure_apps_postfix_domain_name`(string): The system's dns domain name.
- `configure_apps_postfix_external_hostname`(string): The host name that is used to talk to the system.
- `configure_apps_postfix_relay_port`(number): The port that is used to talk to the system; default: `25`.
- `configure_apps_postfix_use_relay_host`(bool): Toggles if a SMTP relay host should be used; default: `false`.
- `configure_apps_postfix_relay_host`(string): The SMTP relay hostname.
- `configure_apps_postfix_relay_username`(string): The SMTP relay username.
- `configure_apps_postfix_relay_password`(string): The SMTP relay password.

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

---

# roles/configure_keycloak_saml/README.md

Configure Keycloak SAML
=========

This role configures Keycloak as SAML provider.

Requirements
------------

none

Role Variables
--------------

- `configure_keycloak_saml_basedn`(string): The LDAP base dn.
- `configure_keycloak_saml_sp_base_url`(string): The Service Provider base url.

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

---

# roles/improve_usability_user_config/README.md

Improve usability user configuration
=========

This role improves user configuration.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry

Role Variables
--------------

- `improve_usability_user_config_basedn`(string): The LDAP base domain name.
- `improve_usability_user_config_external_hostname`(string): The host name that is used to talk to the system.
- `improve_usability_user_config_install_apps`(list):  A list of applications to install.
- `improve_usability_user_config_mailprimaryaddress_required`(bool): Toggles if mailPrimaryAddress should be required; default: `false`.
- `improve_usability_user_config_firstname_required`(bool): Toggles if forename should be required; default: `false`.
- `improve_usability_user_config_wizard_disabled`(string): Toggles the wizard. When set to `Yes`, wizard is enabled; default: `No`.

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

---

# roles/set_dns_glue_record/README.md

Set DNS Glue record
=========

Set a DNS Nameserver Glue record.

Requirements
------------

none

Role Variables
--------------

- `set_dns_glue_record_create_external_hostname_glue_record`(bool): If set to `true` a DNS Glue record is set if not already exists; default: `true
- `set_dns_glue_record_fqdn`(string): Use this variable if remotes hostname is only available as FQDN or set `set_dns_glue_record_host_name`directly.
- `set_dns_glue_record_host_name`(string): Use this variable for remotes hostname otherwise use `set_dns_glue_record_fqdn` for FQDN hostnames.
- `set_dns_glue_record_domain_name`(string): Use this variable to set remotes domain name or set `set_dns_glue_record_superordinate`directly.
- `set_dns_glue_record_basedn`(string):  Use this variable to set remotes base domain name or set `set_dns_glue_record_superordinate`directly.
- `set_dns_glue_record_superordinate`(string): Define superordinate user use `set_dns_glue_record_domain_name` and `set_dns_glue_record_basedn`.
- `set_dns_glue_record_glue_record_nameserver`(string): The target nameserver as FQDN that is used to resolve the external hostname.

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

---

# roles/ucs_add_admin_user/README.md

Add UCS admin user
=========

This role adds an administrative UCS user.

Requirements
------------

none

Role Variables
--------------

- `ucs_add_admin_user_basedn`(string): The LDAP base domain name.
- `ucs_add_admin_user_username`(string): The username for the administrative user.
- `ucs_add_admin_user_firstname`(string): The firstname for the administrative user.
- `ucs_add_admin_user_lastname`(string): The lastname for the administrative user.
- `ucs_add_admin_user_password`(string): The password for the administrative user.
- `ucs_add_admin_user_recoveryemail`(string): The recovery email address for the administrative user.

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

---

# roles/portal_deactivate_category/README.md

Deactivate portal category
=========

This role deactivates a portal category.

Requirements
------------

none

Role Variables
--------------

- `portal_deactivate_category_base_dn`(string): The base DN that has been used when setting up the UCS server
- `portal_deactivate_category_categories`(map): The portal categories map.
- `portal_deactivate_category_install_list`(list): Combine apps/services/customization lists.

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
---

# roles/install_lets_encrypt/README.md

Install letsencrypt
=========

This role installs letsencrypt and configures it. It supports letsencrypt staging as well.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry

Role Variables
--------------

- `install_lets_encrypt_use_letsencrypt_staging`(bool): When `false` it uses regular let's encrypt certificates, `true` switches to the staging area for testing purposes; default: `false`.
- `install_lets_encrypt_implement_ugly_letsencrypt_workaround`(bool): Work around bugs in the let's encrypt staging implementation. This patches files in the univention letsencrypt app; default: `false`.
- `install_lets_encrypt_temp_pw_file`(map): Ansible temporary password file.
- `install_lets_encrypt_temp_dir`(map): Ansible temporary dir.
- `install_lets_encrypt_service_version_map`(map): A dictionary that maps service names to specific versions that ought to be installed. See also `install_packages_force_package_upgrade` for a way to upgrade already installed software.
- `install_lets_encrypt_service_name_list`(list): A list containing service names to be installed.  
- `install_lets_encrypt_force_package_upgrade`(bool): If set to true already installed application versions are checked and if the installed version differs from what has been specified in `install_lets_encrypt_service_version_map` that version is installed instead. Choosing `false` results in the role ignoring already installed software and skip installation; default: `false`.
- `install_lets_encrypt_external_hostname`(string): The host name that is used to talk to the system.

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
---

# roles/cleanup_portal/README.md

Cleanup Portal
=========

Remove default and unused portal entries.

Requirements
------------

none

Role Variables
--------------

- `cleanup_portal_basedn`(string): The LDAP base domain name.
- `cleanup_portal_install_services`(list): A list of services to install.
- `cleanup_portal_domain_admin_group`(string): default: `"cn=Domain Admins,cn=groups,{{ cleanup_portal_basedn }}"`.
- `cleanup_portal_portal_dn`(string): default: `"cn=portals,cn=univention,{{ cleanup_portal_basedn }}"`.
- `cleanup_portal_prometheus_dn`(string): default: `'cn=prometheus,cn=entry,{{ cleanup_portal_portal_dn }}'`.
- `cleanup_portal_admin_dashboard_dn`(string): default: `'cn=admin-dashboard,cn=entry,{{ cleanup_portal_portal_dn }}'`.

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

---

# roles/portal_create_entry/README.md

Create portal entry
=========

This role creates a new portal entry.

Requirements
------------

none

Role Variables
--------------

- `portal_create_entry_base_dn`(string): The base DN that has been used when setting up the UCS server
- `portal_create_entry_entries`(map): The portal entries map.
- `portal_create_entry_install_list`(list): Combine apps/services/customization lists.
- `portal_create_entry_member_attribute_map`(map): The member attributes.
- `portal_create_entry_entry_map`(map): The portal entry entries.

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
---

# roles/configure_apps_owncloud/README.md

Configure Owncloud (apps)
=========

Configure UCS app owncloud.

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



License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com
---

# roles/get_installed_apps/README.md

Get installed univention apps
=========

This role sets a fact with installed univention apps.

Requirements
------------

- ansible.utils
  - cli_parse

Role Variables
--------------

none

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

---

# roles/portal_delete_entry/README.md

Delete portal entry
=========

This role deletes a portal entry.

Requirements
------------

none

Role Variables
--------------

- `portal_delete_entry_base_dn`(string): The base DN that has been used when setting up the UCS server
- `portal_delete_entry_entries`(map): The portal entries map.
- `portal_delete_entry_install_list`(list): Combine apps/services/customization lists.

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
---

# roles/configure_nextcloud_saml/README.md

Configure nextcloud SAML
=========

This role configures nextcloud for SAML single server.

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


License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com

---

# roles/install_apps_ox_post/README.md

Post installation steps of OpenXchange (OX)
=========

This role configures OX.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry
- community.crypto
  - openssl_pkcs12
- community.general
  - java_cert    

Role Variables
--------------

- `install_apps_ox_post_basedn`(string): The LDAP base domain name.
- `install_apps_ox_post_external_hostname`(string): The host name that is used to talk to the system.
- `install_apps_ox_post_ox_keystore_passphrase`(string): The passphrase for ox keystore.
- `install_apps_ox_post_ox_drive_default`(string): Toggle OXDrive by setting `0`for disabled and `1` for enabled; default: `0`.

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

---

# roles/portal_create_category/README.md

Create portal category
=========

This role creates a new portal category.

Requirements
------------

none

Role Variables
--------------

- `portal_create_category_base_dn`(string):  The base DN that has been used when setting up the UCS server
- `portal_create_category_categories`(map): The portal categories map.
- `portal_create_category_install_list`(list): Combine apps/services/customization lists.

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

---

# roles/install_packages/README.md

Install packages
=========

This role installs univention apps with/without fixed versions.

Requirements
------------

none

Role Variables
--------------

- `install_packages_app_version_map`(map): A dictionary that maps application names to specific versions that ought to be installed. See also `install_packages_force_package_upgrade` for a way to upgrade already installed software.
- `install_packages_service_name_list`(list): A list containing application names to be installed.
- `install_packages_temp_pw_file`(map): Tempfile object where univention app password is stored.
- `install_packages_force_package_upgrade`(bool): If set to true already installed application versions are checked and if the installed version differs from what has been specified in `install_packages_app_version_map` that version is installed instead. Choosing `false` results in the role ignoring already installed software and skip installation; default: `false`.
- `install_packages_install_apps`(list): A list of applications to install.
- `install_packages_additional_options`(string): Additional option that could be set during install.

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

---

# roles/add_local_user/README.md

Add local user
=========

This role creates a local user and allows login.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `add_local_user_user`(map): A map containing user information:
```
add_local_user_user:
    name:         # username; default; "ansible"
    comment:      # user comment; default: "ansible user"
    password:     # hased password of user; default:  "{{ "ansible"|password_hash('sha512') }}"
    sshkey_file:  # ssh key filename; default: empty
    sshkey:       # ssh key as string; default: empty
```
- `add_local_user_default_shell`(string): Default user shell; default: `/bin/bash`

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
---

# roles/univention_firewall/README.md

Univention firewall rules.

=========
Manage predefined univention-firewall rules.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `univention_firewall_telegraf`(string): Set firewall status of telegraf service; default: `"ACCEPT"`.

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

---

# roles/configure_apps_nextcloud/README.md

Configure Nextcloud (apps)
=========

Configure UCS app nextcloud.

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



License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com
---

# roles/disable_piwik_tracking/README.md

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


License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com
---

# roles/install_univention/README.md

Install packages with univention-install
=========

This role installs packages via `univention-install` wrapper. 

Requirements
------------

none

Role Variables
--------------

- `install_univention_install_name`(string): The name of the package to be installed.

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

---

# roles/configure_ntp_servers/README.md

Configure NTP servers
=========

This role configures NTP timeservers.

Requirements
------------

- univention.ucs_modules
  - univention_config_registry

Role Variables
--------------

- `configure_ntp_servers_timeservers`(list): A list of ntp server addresses; default `["ptbtime1.ptb.de", "ptbtime2.ptb.de", "ptbtime3.ptb.de"]`


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
---

# roles/workaround_acmetiny_upgrade/README.md

Workaround: Use specific acme tiny version
=========

This role downloads and patches acme-tiny.

Requirements
------------

- ansible.posix
  - patch

Role Variables
--------------

`workaround_acmetiny_upgrade_temp_dir`(map): Ansible temporary dir for workaround files.

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

---

# roles/improve_usability_nextcloud/README.md

Improve usability nextcloud
=========

This role disables some unused functionality like: `contacts`, `spreed`, `mail`, `calendar`.

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


License
-------

GNU General Public License v3.0

Author Information
------------------

Univention GmbH
www.univention.com
---

# roles/ldapsearch_user/README.md

LDAPSearch user
=========

This role adds specific LDAPSearch users.

Requirements
------------

none

Role Variables
--------------

- `ldapsearch_user_basedn`(string): The LDAP base DN.
- `ldapsearch_user_nextcloud_password`(string): The password for nextcloud LDAPSearch user.
- `ldapsearch_user_ox_password`(string): The password for OX LDAPSearch user.
- `ldapsearch_user_install_apps`(list): A list of applications to install.

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

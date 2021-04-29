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

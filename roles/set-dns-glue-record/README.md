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

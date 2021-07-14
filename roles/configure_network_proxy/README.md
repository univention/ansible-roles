Configure network proxy
=========

This role configures network proxy via UCR.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry

Role Variables
--------------

- `configure_network_proxy_enabled`(boolean): Toggle network proxy usage
- `configure_network_proxy_http_proxy`(string): The HTTP proxy server, e.g. `http://192.168.1.100:3128`. If the proxy requires authentication, the username and the password can be provided in the format `http://username:password@192.168.1.100:3128`.
- `configure_network_proxy_https_proxy`(string): The HTTPS proxy server, e.g. `https://192.168.1.100:3128`. If the proxy requires authentication, the username and the password can be provided in the format `https://username:password@192.168.1.100:3128`.
- `configure_network_proxy_no_proxy`(string): A comma-separated list of domain names for which the proxy should not be consulted. An exception for a domain like univention.de also applies to a subdomain like apt.univention.de.

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

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
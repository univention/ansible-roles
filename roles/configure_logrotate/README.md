Configure Logrotate
=========

As is defined on the `ucr` the log files are rotated the set number of times
before being removed. This role is used to set those numbers.

Requirements
------------

- univention.ucs_modules
   - univention_config_registry

Role Variables
--------------
- `configure_logrotate_compress`(bool): If this option is activated, log files are compressed during rotation; default: yes
- `configure_logrotate_create`(string): Configures mode, owner and group of a log file after rotation; default: 640 root adm
- `configure_logrotate_missingok`(bool): If this option is activated, proceed without printing an error message if a logfile is missing; default: yes
- `configure_logrotate_notifempty`(bool): If this option is activated, empty logfiles are not rotated; default: yes
- `configure_logrotate_rotate_count`(number): The rotation interval for system log files; default: 12
- `configure_logrotate_rotate_handling`(string): Log files are rotated according to criterion described by `man logrotate.conf`; default: weekly
- `configure_logrotate_syslog_rotate_count`(number): The rotation interval for syslog file; default: 7 * "rotate/count"
- `configure_logrotate_syslog_rotate_handling`(string): Syslog file is rotated according to criterion described by `man logrotate.conf`; default: daily


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

Configure UCS Password Policies
===============================

This role configures password policies via UCR.
A dn of a policy is required.
All users with this plocicy referenced will get these settings.

Requirements
------------

- univention.ucs_modules
    - univention_config_registry
    - univention_directory_manager

Role Variables
--------------

- `configure_password_policies_dn`(string): At least there should be one policy with activated Checks. The full dn is needed; default: not set
- `configure_password_policies_quality_min_lenght`(string): Sets the minimum password length; default: `8`
- `configure_password_policies_quality_required_chars`(string): Sets required chars for setting new passwords; default: `none`
- `configure_password_policies_quality_forbidden_chars`(string): Sets forbidden chars for setting new passwords; default: `none`
- `configure_password_policies_quality_credit_digits`(string): Sets the minimum number of digits in the new password; ; default: `8`
- `configure_password_policies_quality_credit_upper`(string): Sets the minimum number of upper case letters; default: `1`
- `configure_password_policies_quality_credit_other`(string): Sets the minimum number of chars wich are neither digits nor letters; default: `1`
- `configure_password_policies_quality_credit_lower`(string): Sets the minimum number of lower case letters; default: `1`
- `configure_password_policies_quality_mspolicy`(string): Sets the microsoft policy complexity criteria. If `1`,`true` or `yes` this will b eon top of the dafault python-cracklib. If `sufficient` only ms policy complexity will be used and if `false` only python-cracklib will be used. default: `1`

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

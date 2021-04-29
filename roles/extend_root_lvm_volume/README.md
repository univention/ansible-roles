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

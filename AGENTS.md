# Agent Instructions for univention.ucs_roles

## Overview
This repository is an Ansible collection named `univention.ucs_roles` containing roles for bootstrapping and configuring Univention Corporate Server (UCS).

## Development & Workflow
- **Linting**: Use `pre-commit run --all-files` to run `yamllint`, `ansible-lint`, and `flake8`.
- **Testing**:
    - Use `test_get_apps.yaml` as a template for testing specific roles or playbooks.
    - Host definitions for testing can be found in `hosts.yaml`.
- **Dependencies**: Ensure the following collections/modules are available:
    - `univention.ucs_modules >= 1.2.0`
    - `ansible.posix >= 1.0.0`
    - `ansible.utils >= 2.9.0`
    - `community.general >= 6.5.0`
    - `community.crypto >= 2.11.1`

## Architecture
- Roles are located in the `roles/` directory.
- Each role is a standalone component for configuring parts of UCS (e.g., users, services, network).

# Ansible RPMDB Maintenance Role

## Overview

The `ansible_rpmdb_maintenance` role automates the maintenance of the RPM database (`rpmdb`) on Red Hat-based systems. It ensures the integrity and consistency of the package management database, preventing issues related to package installations and updates.

## Features

- **RPM Lock Management**: Detects and removes stale RPM database locks.
- **Database Rebuild**: Automatically rebuilds the RPM database when inconsistencies are detected.
- **Logging**: Records maintenance activities for auditing and troubleshooting purposes.

## Requirements

- **Ansible Version**: 2.9 or higher.
- **Target Systems**: Red Hat-based distributions (e.g., RHEL, CentOS, Fedora).

## Role Variables

The following variables can be customized as needed:

| Variable Name           | Default Value                         | Description                                      |
|-------------------------|---------------------------------------|--------------------------------------------------|
| `rpmdb_maintenance_log` | `/var/log/rpmdb_maintenance.log`      | Path to the log file for maintenance activities. |
| `rpm_lock_file`         | `/var/lib/rpm/.rpm.lock`              | Path to the RPM lock file.                       |
| `rpm_db_path`           | `/var/lib/rpm`                        | Path to the RPM database directory.              |
| `rpm_process_patterns`  | `['yum', 'rpm', 'packagekit']`        | List of process patterns to check for running RPM-related processes. |

## Dependencies

This role has no external dependencies.

## Example Playbook

```yaml
- name: Perform RPMDB Maintenance
  hosts: servers
  roles:
    - role: ansible_rpmdb_maintenance
      vars:
        rpmdb_maintenance_log: /custom/path/rpmdb_maintenance.log
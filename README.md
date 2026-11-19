# Ansible role x2goclient

[![Molecule CI](https://github.com/ajholanda/ansible_role_x2goclient/actions/workflows/molecule.yml/badge.svg)](https://github.com/ajholanda/ansible_role_x2goclient/actions/workflows/molecule.yml)

Ansible role to install or uninstall X2Go client for Linux or Windows.

## Requirements

None.

## Role Variable

- `x2goclient_state`: desired state after running package manager task (default: `present`).

## Notes

- On **RedHat family** distributions (AlmaLinux, RHEL), `epel-release` is installed automatically.
- **AlmaLinux/RHEL >= 10** are skipped for x2goclient installation due to Wayland incompatibility.
- On **openSUSE**, the X2Go repository is added automatically before installing the client.

- `package_state`: set a default value that can be used as a global variable across roles [ajholanda roles](https://galaxy.ansible.com/ajholanda). 
- `x2goclient_state`: desired state after running package manager task.
## Dependencies

None.

## Example Playbook

```
    - hosts: all
      roles:
        - ajholanda.x2goclient
```

To uninstall

```
    - hosts: all
      vars:
        x2goclient_state: absent
      roles:
        - ajholanda.x2goclient
```

## License

MIT.

## Author Information

[Adriano J. Holanda](https://ajholanda.github.io).

# Ansible role x2goclient
Ansible role to install or uninstall X2Go client for Linux or Windows.

## Requirements

None.

## Role Variables

- `x2goclient_install: True`: boolean value to control the installation process.
	- `True` - install
	- `False` - uninstall

## Dependencies

None.

## Example Playbook

    - hosts: all
      roles:
        - ajholanda.ansible_role_x2goclient

## License

MIT.

## Author Information

[Adriano J. Holanda](https://ajholanda.github.io).

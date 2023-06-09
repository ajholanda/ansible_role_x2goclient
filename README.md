# Ansible role x2goclient
Ansible role to install or uninstall X2Go client for Linux or Windows.

## Requirements

None.

## Role Variables

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

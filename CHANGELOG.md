# Changes by release

## [1.4.0] 2026-11-18

- Delete variable `package_state`.
- Add `Dockerfile.j2` to build custom Molecule test images supporting apt, microdnf, and zypper package managers.
- Update `molecule/default/molecule.yml` to use `almalinux:9-minimal` with custom `Dockerfile.j2` instead of pre-built geerlingguy images.
- Refactor RHEL condition in `tasks/main.yml` to use `ansible_facts['distribution']`; skip x2goclient install on RedHat family >= version 10 (Wayland incompatibility).
- Add `gather_facts: true` and `become: false` to `molecule/default/converge.yml`.
- Add `almalinux`, `rocky`, and `rhel` Galaxy tags in `meta/main.yml`.

## [1.3.0] 2025-06-20

- Use namespace in the modules.
- Fix the value type of versions.

## [1.1.0] 2023-05-18

- Add variable `package_state` to be used as default and generalized package state value.


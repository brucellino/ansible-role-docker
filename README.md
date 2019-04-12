# Docker role

This role provides Docker on an Ubuntu bionic base, intended for a Jenkins build host.

## Requirements

A working OS and a sudo enabled user are required. The role is expected to be applied on something like a vanilla Ubuntu AMI.

## Role Variables

Variables are described in `default/main.yml`. They include:

- `deb_repositories`: List of repositories to be enabled.
- `base_packages`: OS packages to be installed from the repositories
- `packages`: Extra packages for specific purposes
- `gems`: Ruby Gems to be added to the Gemfile
- `docker`: Variables necessary to have the Docker Engine present
- `npm`: NPM packages and Node tools

## Dependencies

The EC2 module requires the boto pip module.

## Example Playbook

```
- hosts: localhost
  roles:
      - { role: brucellino.docker, become: true }
```

## License

Apache 2.0

## Author Information

[@brucellino](https://github.com/brucellino)

# Base Platform

This role provides the base platform for a Jenkins build host.

## Requirements

Just a working OS and a sudo enabled user are required. The role is expected to be applied on something like a vanilla Ubuntu AMI.

## Role Variables

Variables are described in `default/main.yml`. They include:

- `deb_repositories`: List of repositories to be enabled.
- `base_packages`: OS packages to be installed from the repositories
- `packages`: Extra packages for specific purposes
- `gems`: Ruby Gems to be added to the Gemfile
- `docker`: Variables necessary to have the Docker Engine present
- `npm`: NPM packages and Node tools


## Dependencies

None

## Example Playbook

```
- hosts: localhost
  roles:
      - { role: base-platform, become: true }
```

## License

Apache 2.0

## Author Information

[@brucellino](https://github.com/brucellino)
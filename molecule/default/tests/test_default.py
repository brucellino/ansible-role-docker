import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_docker(host):
    pkg = host.package('docker-ce')
    assert pkg.is_installed
    docker_service = host.service('docker')
    assert docker_service.is_running
    assert docker_service.is_enabled

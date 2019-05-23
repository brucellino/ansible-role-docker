import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_os_packages(host):
    docker_py = host.pip_package.get_packages()
    assert "docker-py" not in docker_py

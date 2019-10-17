import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("module", [
    ("redis"),
    ("inotify")
])
def test_pecl_module_installed(host, module):
    cmd = host.run("php -m")
    assert cmd.rc == 0
    assert module in cmd.stdout

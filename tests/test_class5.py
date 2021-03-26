import re
import pytest
from pathlib import Path

from utilities import subprocess_runner, remove_ansible_warnings

TEST_CASES = [
    "../class5/collateral/cli_config/cli_config1.yml",
    "../class5/collateral/cli_config/cli_config2.yml",
    "../class5/collateral/cli_config/cli_config3.yml",
    "../class5/collateral/collections/coll_pb1.yml",
    "../class5/collateral/collections/coll_pb2.yml",
    "../class5/collateral/hierarchy/eos_config.yml",
    "../class5/collateral/hierarchy/ios_config1.yml",
    "../class5/collateral/hierarchy/ios_config2.yml",
    "../class5/collateral/ios_config/ios_config1.yml",
    "../class5/collateral/ios_config/ios_config2.yml",
    "../class5/collateral/ios_config/ios_config3.yml",
    "../class5/collateral/ios_config/ios_config4.yml",
    "../class5/collateral/ios_config/ios_config5.yml",
    "../class5/collateral/ios_config/ios_config6.yml",
    "../class5/collateral/ios_config/ios_config7.yml",
    "../class5/collateral/ios_config/show_cmd.yml",
    "../class5/collateral/jinja2_config/cfg_jinja.yml",
    "../class5/collateral/junos_config/junos_config1.yml",
    "../class5/collateral/nxos_config/nxos_config1.yml",
    "../class5/collateral/ssh_keys/ios_config1.yml",
]


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_runner_collateral(test_case):
    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]
    cmd_list = ["ansible-playbook", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, script_dir)
    std_err = remove_ansible_warnings(std_err)
    assert return_code == 0
    assert std_err == ""


def test_class5_ex1():

    base_path = "../class5/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml", "-f 12"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)

    assert "TASK [IOS global config]" in std_out
    assert "TASK [IOS-XE global config]" in std_out
    assert "TASK [EOS global config]" in std_out
    assert "TASK [NX-OS global config]" in std_out
    assert "TASK [Juniper global config]" in std_out
    for device in [
        "cisco1",
        "cisco2",
        "cisco5",
        "cisco6",
        "arista5",
        "arista6",
        "arista7",
        "arista8",
        "nxos1",
        "nxos2",
        "vmx1",
        "vmx2",
    ]:
        assert std_out.count(device) == 7

    assert std_err == ""
    assert return_code == 0


def test_class5_ex1_idempotent():
    """Run test again to verify idempotency."""
    base_path = "../class5/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml", "-f 12"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    for device in [
        "cisco1",
        "cisco2",
        "cisco5",
        "cisco6",
        "arista5",
        "arista6",
        "arista7",
        "arista8",
        "nxos1",
        "nxos2",
        "vmx1",
        "vmx2",
    ]:
        pattern = rf"^{device}.*changed=0 .*$"
        assert re.search(pattern, std_out, flags=re.M)


def test_class5_ex2():
    base_path = "../class5/exercises/exercise2"
    cmd_list = ["ansible-playbook", "exercise2.yml", "-f 12"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0

    # Should be idempotent as would have been configured in exercise1.
    for device in [
        "cisco1",
        "cisco2",
        "cisco5",
        "cisco6",
        "arista5",
        "arista6",
        "arista7",
        "arista8",
        "nxos1",
        "nxos2",
        "vmx1",
        "vmx2",
    ]:
        pattern = rf"^{device}.*changed=0 .*$"
        assert re.search(pattern, std_out, flags=re.M)


def test_class5_ex3a():
    base_path = "../class5/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3a.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_out.count("permit") == 20
    assert std_err == ""
    assert return_code == 0


def test_class5_ex3b():
    base_path = "../class5/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3b.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_out.count("permit") == 18
    assert std_out.count("deny") == 2
    assert std_err == ""
    assert return_code == 0


def test_class5_ex4():
    base_path = "../class5/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert "TASK [Generate interface configuration]" in std_out
    assert "TASK [Generate BGP configuration]" in std_out
    assert "TASK [Assemble the two parts into one configuration change file]" in std_out
    assert "TASK [Deploy configurations to devices]" in std_out
    assert "BGP router identifier 172.31.101.101, local AS number 22" in std_out
    assert "BGP router identifier 172.31.101.102, local AS number 22" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class5_ex5():
    base_path = "../class5/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5.yml", "-i", "./ansible-hosts.ini"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_out.count("student1") == 2
    assert std_err == ""
    assert return_code == 0

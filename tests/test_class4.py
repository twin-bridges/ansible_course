import os
import pytest
from pathlib import Path

from utilities import subprocess_runner, remove_ansible_warnings


TEST_CASES = [
    "../class4/collateral/assert/assert.yml",
    "../class4/collateral/eos_feature/l2_intf.yml",
    "../class4/collateral/eos_feature/show_intf.yml",
    "../class4/collateral/handlers_wrmem/nxos_vlan_1.yml",
    "../class4/collateral/handlers_wrmem/nxos_vlan_2.yml",
    "../class4/collateral/handlers_wrmem/nxos_vlan_3.yml",
    "../class4/collateral/ios_feature/banner.yml",
    "../class4/collateral/ios_feature/ios_bgp.yml",
    "../class4/collateral/ios_feature/test_ping.yml",
    "../class4/collateral/net_modules/net_l2_intf.yml",
    "../class4/collateral/net_modules/net_ping.yml",
    "../class4/collateral/nxos_feature/show_intf.yml",
    "../class4/collateral/nxos_feature/l2_intf.yml",
    "../class4/collateral/resource_modules/interfaces/interfaces_ios.yml",
    "../class4/collateral/resource_modules/interfaces/interfaces_nxos.yml",
    "../class4/collateral/resource_modules/interfaces/interfaces_simple.yml",
    "../class4/collateral/resource_modules/interfaces/show_intf.yml",
    "../class4/collateral/resource_modules/l2_interfaces/l2_eos.yml",
    "../class4/collateral/resource_modules/l2_interfaces/l2_nxos.yml",
    "../class4/collateral/resource_modules/l2_interfaces/show_intf.yml",
    "../class4/collateral/resource_modules/l3_interfaces/l3_eos.yml",
    "../class4/collateral/resource_modules/l3_interfaces/l3_ios.yml",
    "../class4/collateral/resource_modules/l3_interfaces/l3_nxos.yml",
    "../class4/collateral/resource_modules/l3_interfaces/show_intf.yml",
    "../class4/collateral/resource_modules/vlans/vlans_eos.yml",
    "../class4/collateral/resource_modules/vlans/vlans_eos_override.yml",
    "../class4/collateral/resource_modules/vlans/vlans_nxos.yml",
    "../class4/collateral/resource_modules_facts/eos_facts.yml",
    "../class4/collateral/resource_modules_facts/ios_facts.yml",
    "../class4/collateral/resource_modules_facts/junos_facts.yml",
    "../class4/collateral/resource_modules_facts/nxos_facts.yml",
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


def test_class4_ex1():
    base_path = "../class4/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0


def test_class4_ex2():
    base_path = "../class4/exercises/exercise2"
    cmd_list = ["ansible-playbook", "exercise2.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0


def test_class4_ex3():
    base_path = "../class4/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0


def test_class4_ex4():
    base_path = "../class4/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0


def test_class4_ex5():
    # Deprecated module will generate an ansible warning on std_err (disable that)
    os.environ["ANSIBLE_DEPRECATION_WARNINGS"] = "False"
    base_path = "../class4/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0
    os.environ.pop("ANSIBLE_DEPRECATION_WARNINGS")

import re
import pytest
from pathlib import Path
from utilities import subprocess_runner, remove_ansible_warnings


TEST_CASES = [
    "../class7/collateral/hostvars/hostvars1.yml",
    "../class7/collateral/hostvars/hostvars2.yml",
    "../class7/collateral/block/block_ex1.yml",
    "../class7/collateral/block/block_ex2.yml",
    "../class7/collateral/block/block_ex3.yml",
    "../class7/collateral/pipe/eos_pipe.yml",
    "../class7/collateral/pipe/eos_pipe2.yml",
    "../class7/collateral/pipe/nxos_pipe.yml",
    "../class7/collateral/textfsm/textfsm1.yml",
    "../class7/collateral/textfsm/textfsm2.yml",
    "../class7/collateral/textfsm/textfsm3.yml",
    "../class7/collateral/genie/genie_module.yml",
    "../class7/collateral/genie/genie_filter.yml",
    "../class7/collateral/regex/regex_test1.yml",
    "../class7/collateral/regex/regex_test2.yml",
    "../class7/collateral/regex/regex_test3.yml",
    "../class7/collateral/dynamic_inventory/vlans_eos.yml",
    "../class7/collateral/dynamic_inventory/test_pb.yml",
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


def test_class7_ex1():
    base_path = "../class7/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert "nxos1                      : ok=7" in std_out
    assert "nxos2                      : ok=7" in std_out
    assert re.search(r"nxos1.*failed=0", std_out)
    assert re.search(r"nxos2.*failed=0", std_out)


def test_class7_ex2():
    base_path = "../class7/exercises/exercise2"
    cmd_list = ["ansible-playbook", "exercise2.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"arista5.*ok=1 ", std_out)
    assert re.search(r"arista6.*ok=1 ", std_out)
    assert re.search(r"arista7.*ok=1 ", std_out)
    assert re.search(r"arista8.*ok=1 ", std_out)
    assert re.search(r"arista5.*rescued=1 ", std_out)
    assert re.search(r"arista6.*rescued=1 ", std_out)
    assert re.search(r"arista7.*rescued=1 ", std_out)
    assert re.search(r"arista8.*rescued=1 ", std_out)


def test_class7_ex3a():
    base_path = "../class7/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3a.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"nxos1.*ok=4 ", std_out)
    assert re.search(r"nxos2.*ok=4 ", std_out)


def test_class7_ex3b():
    base_path = "../class7/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3b.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"arista5.*ok=6 ", std_out)
    assert re.search(r"arista6.*ok=6 ", std_out)
    assert re.search(r"arista7.*ok=6 ", std_out)
    assert re.search(r"arista8.*ok=6 ", std_out)


def test_class7_ex4a():
    base_path = "../class7/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4a.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"nxos1.*ok=4 ", std_out)
    assert re.search(r"nxos2.*ok=4 ", std_out)


def test_class7_ex4b():
    base_path = "../class7/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4b.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"nxos1.*ok=4 ", std_out)
    assert re.search(r"nxos2.*ok=4 ", std_out)


def test_class7_ex5a():
    base_path = "../class7/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5a.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"nxos1.*ok=5 ", std_out)
    assert re.search(r"nxos2.*ok=5 ", std_out)


def test_class7_ex5b():
    base_path = "../class7/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5b.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"arista5.*ok=5 ", std_out)
    assert re.search(r"arista6.*ok=5 ", std_out)
    assert re.search(r"arista7.*ok=5 ", std_out)
    assert re.search(r"arista8.*ok=5 ", std_out)


def test_class7_ex6():
    base_path = "../class7/exercises/exercise6"
    cmd_list = ["ansible-inventory", "--graph", "-i", "./dyn_inv.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert "@arista" in std_out
    assert "@cisco" in std_out
    assert "@juniper" in std_out
    assert "@local" in std_out
    assert "@nxos" in std_out

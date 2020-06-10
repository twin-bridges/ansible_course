import re
import pytest
from pathlib import Path
from utilities import subprocess_runner, remove_ansible_warnings


TEST_CASES = [
    "../bonus2/collateral/upgrade_os/put_file.yml",
    "../bonus2/collateral/upgrade_os/file_system.yml",
    "../bonus2/collateral/filters/my_pb.yml",
    "../bonus2/collateral/filters/show_ip_int_br.yml",
    "../bonus2/collateral/filters_role/test_filters.yml",
    "../bonus2/collateral/modules/test1.yml",
    "../bonus2/collateral/modules/test_netmiko.yml",
    "../bonus2/collateral/modules/broken.yml",
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


def test_bonus2_ex1():
    base_path = "../bonus2/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    std_out = std_out.lower()
    assert std_out.count("hello world") == 3


def test_bonus2_ex2():
    base_path = "../bonus2/exercises/exercise2"
    cmd_list = ["ansible-playbook", "exercise2.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    for hostname in (
        "arista5",
        "arista6",
        "arista7",
        "arista8",
    ):
        assert re.search(rf"{hostname}.*ok=3.*failed=0 ", std_out)


def test_bonus2_ex3():
    base_path = "../bonus2/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    for hostname in (
        "cisco1",
        "cisco2",
        "cisco5",
        "cisco6",
    ):
        assert re.search(rf"{hostname}.*ok=3.*failed=0 ", std_out)


def test_bonus2_ex4():
    base_path = "../bonus2/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"localhost.*ok=1.*failed=0 ", std_out)


def test_bonus2_ex5():
    base_path = "../bonus2/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"cisco1.*ok=1.*changed=1.*failed=0 ", std_out)

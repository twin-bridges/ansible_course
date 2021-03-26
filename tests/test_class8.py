import re
import pytest
from pathlib import Path
from utilities import subprocess_runner, remove_ansible_warnings


TEST_CASES = [
    "../class8/collateral/lookups/lookup_examples.yml",
    "../class8/collateral/filters/filters_map.yml",
    "../class8/collateral/filters/filters_set.yml",
    "../class8/collateral/filters/filters1.yml",
    "../class8/collateral/callbacks/test.yml",
    "../class8/collateral/data_structures/zip_and_combine.yml",
    "../class8/collateral/data_structures/zip_and_dict1.yml",
    "../class8/collateral/data_structures/zip_and_dict2.yml",
    "../class8/collateral/data_structures/list_concatenation.yml",
    "../class8/collateral/data_structures/textfsm_combine.yml",
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


def test_class8_ex1():
    base_path = "../class8/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"nxos1.*ok=4", std_out)
    assert re.search(r"nxos2.*ok=4", std_out)


def test_class8_ex2():
    base_path = "../class8/exercises/exercise2"
    cmd_list = ["ansible-playbook", "exercise2.yml", "-i", "./ansible-hosts.ini"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    for switch in ("arista5", "arista6", "arista7", "arista8"):
        assert re.search(rf"{switch}.*ok=2.*failed=0", std_out)


def test_class8_ex3():
    base_path = "../class8/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    for switch in ("arista5", "arista6", "arista7", "arista8"):
        assert re.search(rf"{switch}.*ok=6.*failed=0", std_out)


def test_class8_ex4():
    base_path = "../class8/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    for switch in ("arista5", "arista6", "arista7", "arista8"):
        assert re.search(rf"{switch}.*ok=6.*failed=0", std_out)


def test_class8_ex5():
    base_path = "../class8/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"nxos1.*ok=8", std_out)
    assert re.search(r"nxos2.*ok=7", std_out)


def test_class8_ex6a():
    """Exercise 6a doesn't actually fail."""
    base_path = "../class8/exercises/exercise6"
    cmd_list = ["ansible-playbook", "exercise6a.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"msg.*show_lldp", std_out)


def test_class8_ex6f():
    """Exercise 6f doesn't actually fail."""
    base_path = "../class8/exercises/exercise6"
    cmd_list = ["ansible-playbook", "exercise6f.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"msg.*parse_cli_textfsm.fsm_template.", std_out)


@pytest.mark.parametrize(
    "playbook",
    [
        "exercise6b.yml",
        "exercise6c.yml",
        "exercise6d.yml",
        "exercise6e.yml",
        "exercise6g.yml",
    ],
)
def test_class8_ex6_errors(playbook):
    """Each of these tests should have errors on std_err."""
    base_path = "../class8/exercises/exercise6"
    cmd_list = ["ansible-playbook", playbook]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert return_code != 0


@pytest.mark.parametrize(
    "playbook",
    [
        "exercise6a_fixed.yml",
        "exercise6b_fixed.yml",
        "exercise6c_fixed.yml",
        "exercise6d_fixed.yml",
        "exercise6e_fixed.yml",
        "exercise6f_fixed.yml",
        "exercise6g_fixed.yml",
    ],
)
def test_class8_ex6_fixed(playbook):
    base_path = "../class8/exercises/exercise6/solutions"
    cmd_list = ["ansible-playbook", playbook]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0


def test_class8_ex7a():
    """Should fail when no vault password is provided."""
    base_path = "../class8/exercises/exercise7"
    cmd_list = ["ansible-playbook", "exercise7.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert return_code != 0


def test_class8_ex7b():
    """Should fail when no vault password is provided."""
    base_path = "../class8/exercises/exercise7"
    cmd_list = [
        "ansible-playbook",
        "exercise7.yml",
        "--vault-password-file",
        ".my_vault",
    ]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert return_code == 0
    assert std_err == ""
    for switch in ("arista5", "arista6", "arista7", "arista8"):
        assert re.search(rf"{switch}.*ok=2.*failed=0", std_out)
    assert std_out.count("130.126.24.24") == 4
    assert std_out.count("bogus.com") == 4

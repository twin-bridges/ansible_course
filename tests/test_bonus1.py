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


def test_bonus1_ex1():
    base_path = "../bonus1/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"arista5.*ok=4.*failed=0 ", std_out)
    for hostname in (
        "arista6",
        "arista7",
        "arista8",
        "cisco1",
        "cisco2",
        "cisco5",
        "cisco6",
        "nxos1",
        "nxos2",
    ):
        assert re.search(rf"{hostname}.*ok=3.*failed=0 ", std_out)
    

def test_bonus1_ex2():
    base_path = "../bonus1/exercises/exercise2"
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
        "cisco1",
        "cisco2",
        "cisco5",
        "cisco6",
    ):
        assert re.search(rf"{hostname}.*ok=3.*failed=0 ", std_out)



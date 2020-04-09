import subprocess
import re
import pytest
from pathlib import Path


TEST_CASES = [
    "../class8/collateral/lookups/lookup_examples.yml",
#    "../class7/collateral/hostvars/hostvars1.yml",
]

"""
./class8/collateral/filters/filters_map.yml
./class8/collateral/filters/filters_set.yml
./class8/collateral/filters/ip_addresses.yml
./class8/collateral/filters/filters1.yml
./class8/collateral/callbacks/test.yml
./class8/collateral/callbacks/test_fail.yml
./class8/collateral/callbacks/filters1.yml
./class8/collateral/data_structures/zip_and_combine.yml
./class8/collateral/data_structures/zip_and_dict1.yml
./class8/collateral/data_structures/zip_and_dict2.yml
./class8/collateral/data_structures/list_concatenation.yml
./class8/collateral/data_structures/textfsm_combine.yml
./class8/collateral/debug_tshoot/debug1_fail_auth.yml
./class8/collateral/debug_tshoot/debug2_invalid_hostname.yml
./class8/collateral/debug_tshoot/debug3_invalid_cmd.yml
./class8/collateral/debug_tshoot/debug6_missing_lib.yml
./class8/collateral/debug_tshoot/debug4_bad_escaping.yml
./class8/collateral/debug_tshoot/debug5_missing_module.yml
./class8/collateral/debug_tshoot/debug7_indentation.yml
./class8/collateral/debug_tshoot/debug8_debugger.yml
./class8/collateral/vault/vault1.yml
./class8/collateral/vault/creds.yml
./class8/collateral/vault/vault2.yml
"""


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def remove_ansible_warnings(std_err):
    """Remove the specified warnings from std_err."""
    warning_list = [
        r"^.WARNING.: Ignoring timeout.10. for .*$",
    ]

    # Remove warnings one at a time from std_err
    for ansible_warn in warning_list:
        std_err = re.sub(ansible_warn, "", std_err, flags=re.M)
    return std_err.strip()


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


#def test_class7_ex1():
#    base_path = "../class7/exercises/exercise1"
#    cmd_list = ["ansible-playbook", "exercise1.yml"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    std_err = remove_ansible_warnings(std_err)
#    assert std_err == ""
#    assert return_code == 0
#    assert "nxos1                      : ok=7" in std_out
#    assert "nxos2                      : ok=7" in std_out
#    assert re.search(r"nxos1.*failed=0", std_out)
#    assert re.search(r"nxos2.*failed=0", std_out)
#
#
#def test_class7_ex2():
#    base_path = "../class7/exercises/exercise2"
#    cmd_list = ["ansible-playbook", "exercise2.yml"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    std_err = remove_ansible_warnings(std_err)
#    assert std_err == ""
#    assert return_code == 0
#    assert re.search(r"arista5.*ok=1 ", std_out)
#    assert re.search(r"arista6.*ok=1 ", std_out)
#    assert re.search(r"arista7.*ok=1 ", std_out)
#    assert re.search(r"arista8.*ok=1 ", std_out)
#    assert re.search(r"arista5.*rescued=1 ", std_out)
#    assert re.search(r"arista6.*rescued=1 ", std_out)
#    assert re.search(r"arista7.*rescued=1 ", std_out)
#    assert re.search(r"arista8.*rescued=1 ", std_out)
#
#
#def test_class7_ex3a():
#    base_path = "../class7/exercises/exercise3"
#    cmd_list = ["ansible-playbook", "exercise3a.yml"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    std_err = remove_ansible_warnings(std_err)
#    assert std_err == ""
#    assert return_code == 0
#    assert re.search(r"nxos1.*ok=4 ", std_out)
#    assert re.search(r"nxos2.*ok=4 ", std_out)
#
#def test_class7_ex3b():
#    base_path = "../class7/exercises/exercise3"
#    cmd_list = ["ansible-playbook", "exercise3b.yml"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    std_err = remove_ansible_warnings(std_err)
#    assert std_err == ""
#    assert return_code == 0
#    assert re.search(r"arista5.*ok=6 ", std_out)
#    assert re.search(r"arista6.*ok=6 ", std_out)
#    assert re.search(r"arista7.*ok=6 ", std_out)
#    assert re.search(r"arista8.*ok=6 ", std_out)
#
#def test_class7_ex4a():
#    base_path = "../class7/exercises/exercise4"
#    cmd_list = ["ansible-playbook", "exercise4a.yml"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    std_err = remove_ansible_warnings(std_err)
#    assert std_err == ""
#    assert return_code == 0
#    assert re.search(r"nxos1.*ok=4 ", std_out)
#    assert re.search(r"nxos2.*ok=4 ", std_out)
#
#def test_class7_ex4b():
#    base_path = "../class7/exercises/exercise4"
#    cmd_list = ["ansible-playbook", "exercise4b.yml"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    std_err = remove_ansible_warnings(std_err)
#    assert std_err == ""
#    assert return_code == 0
#    assert re.search(r"nxos1.*ok=4 ", std_out)
#    assert re.search(r"nxos2.*ok=4 ", std_out)
#
#def test_class7_ex5a():
#    base_path = "../class7/exercises/exercise5"
#    cmd_list = ["ansible-playbook", "exercise5a.yml"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    std_err = remove_ansible_warnings(std_err)
#    assert std_err == ""
#    assert return_code == 0
#    assert re.search(r"nxos1.*ok=5 ", std_out)
#    assert re.search(r"nxos2.*ok=5 ", std_out)
#
#def test_class7_ex5b():
#    base_path = "../class7/exercises/exercise5"
#    cmd_list = ["ansible-playbook", "exercise5b.yml"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    std_err = remove_ansible_warnings(std_err)
#    assert std_err == ""
#    assert return_code == 0
#    assert re.search(r"arista5.*ok=5 ", std_out)
#    assert re.search(r"arista6.*ok=5 ", std_out)
#    assert re.search(r"arista7.*ok=5 ", std_out)
#    assert re.search(r"arista8.*ok=5 ", std_out)
#
#def test_class7_ex6():
#    base_path = "../class7/exercises/exercise6"
#    cmd_list = ["ansible-inventory", "--graph", "-i", "./dyn_inv.py"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    std_err = remove_ansible_warnings(std_err)
#    assert std_err == ""
#    assert return_code == 0
#    assert "@arista" in std_out
#    assert "@cisco" in std_out
#    assert "@juniper" in std_out
#    assert "@local" in std_out
#    assert "@nxos" in std_out

import re
import pytest
from pathlib import Path
from utilities import subprocess_runner, remove_ansible_warnings


TEST_CASES = [
    "../bonus1/collateral/napalm_getters/napalm_get_ios.yml",
    "../bonus1/collateral/napalm_getters/napalm_get_eos.yml",
    "../bonus1/collateral/napalm_getters/napalm_get_junos.yml",
    "../bonus1/collateral/napalm_getters/napalm_get_nxos.yml",
    "../bonus1/collateral/napalm_getters/napalm_get_nxos_ssh.yml",
    "../bonus1/collateral/napalm_getters_addl/napalm_get_arp.yml",
    "../bonus1/collateral/napalm_getters_addl/napalm_bgp.yml",
    "../bonus1/collateral/napalm_getters_mp/napalm_lldp.yml",
    "../bonus1/collateral/napalm_ping/napalm_ping.yml",
    "../bonus1/collateral/napalm_merge/napalm_merge_1a.yml",
    "../bonus1/collateral/napalm_merge/napalm_merge_1b.yml",
    "../bonus1/collateral/napalm_merge/napalm_merge_2.yml",
    "../bonus1/collateral/napalm_replace/napalm_get_config.yml",
    "../bonus1/collateral/napalm_replace/napalm_get_checkpoint.yml",
    "../bonus1/collateral/napalm_replace/napalm_replace_ios.yml",
    "../bonus1/collateral/napalm_replace/napalm_replace_junos.yml",
    "../bonus1/collateral/napalm_replace/napalm_replace_nxos.yml",
    "../bonus1/collateral/napalm_templating/napalm_get_config.yml",
    "../bonus1/collateral/napalm_templating/gen_config_1.yml",
    "../bonus1/collateral/napalm_templating/gen_config_2.yml",
    "../bonus1/collateral/napalm_templating/gen_config_3.yml",
    "../bonus1/collateral/napalm_templating/gen_config_4.yml",
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


def test_bonus1_ex3():
    base_path = "../bonus1/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    for hostname in ("arista5",):
        assert re.search(rf"{hostname}.*ok=4.*failed=0 ", std_out)


def test_bonus1_ex4():
    base_path = "../bonus1/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    for hostname in (
        "nxos1",
        "nxos2",
    ):
        assert re.search(rf"{hostname}.*ok=6.*failed=0 ", std_out)


def test_bonus1_ex5():
    base_path = "../bonus1/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    for hostname in ("arista5",):
        assert re.search(rf"{hostname}.*ok=2.*failed=0 ", std_out)

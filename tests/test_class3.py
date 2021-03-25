import pytest
from pathlib import Path

from utilities import subprocess_runner, remove_ansible_warnings


TEST_CASES = [
    "../class3/collateral/conditionals/test_when_1.yml",
    "../class3/collateral/conditionals/test_when_2.yml",
    "../class3/collateral/conditionals/test_when_3.yml",
    "../class3/collateral/conditionals/test_when_4.yml",
    "../class3/collateral/conditionals/test_when_5.yml",
    "../class3/collateral/conditionals/test_when_6.yml",
    "../class3/collateral/conditionals/test_when_7.yml",
    "../class3/collateral/conditionals/test_when_8.yml",
    "../class3/collateral/conditionals/test_when_9.yml",
    "../class3/collateral/jinja2/j2_conditional.yml",
    "../class3/collateral/jinja2/j2_includes.yml",
    "../class3/collateral/jinja2/j2_loop.yml",
    "../class3/collateral/jinja2/j2_loop_dict.yml",
    "../class3/collateral/jinja2/j2_test.yml",
    "../class3/collateral/jinja2_modular/j2_test.yml",
    "../class3/collateral/loops/loop_1.yml",
    "../class3/collateral/loops/loop_2.yml",
    "../class3/collateral/loops/loop_3.yml",
    "../class3/collateral/loops_and_when/loop_and_when_1.yml",
    "../class3/collateral/loops_and_when/loop_and_when_2.yml",
    "../class3/collateral/loops_dict/loops_dict_1.yml",
    "../class3/collateral/loops_dict/loops_dict_2.yml",
    "../class3/collateral/loops_dict/loops_dict_3.yml",
    "../class3/collateral/loops_dict/loops_dict_4.yml",
    "../class3/collateral/tags_limit/ios_config_ex.yml",
    "../class3/collateral/tags_limit/ios_example.yml",
    "../class3/collateral/tags_limit/retrieve_ntp.yml",
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


def test_class3_ex1a():
    base_path = "../class3/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1a.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "arista5                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2"
        in std_out
    )
    assert (
        "arista6                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2"
        in std_out
    )
    assert (
        "arista7                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2"
        in std_out
    )
    assert (
        "arista8                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2"
        in std_out
    )
    assert (
        "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    skipped=3"
        in std_out
    )
    assert (
        "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    skipped=3"
        in std_out
    )
    assert (
        "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    skipped=3"
        in std_out
    )
    assert (
        "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    skipped=3"
        in std_out
    )
    assert (
        "vmx1                       : ok=1    changed=0    unreachable=0    failed=0    skipped=3"
        in std_out
    )
    assert (
        "vmx2                       : ok=1    changed=0    unreachable=0    failed=0    skipped=3"
        in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class3_ex1b_eos():
    base_path = "../class3/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1b.yml", "--tags", "eos"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "arista5                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert (
        "arista6                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert (
        "arista7                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert (
        "arista8                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class3_ex1b_ios():
    base_path = "../class3/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1b.yml", "--tags", "ios"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert (
        "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert (
        "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert (
        "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class3_ex1b_junos():
    base_path = "../class3/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1b.yml", "--tags", "junos"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "vmx1                       : ok=1    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert (
        "vmx2                       : ok=1    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class3_ex2():
    base_path = "../class3/exercises/exercise2"
    cmd_list = ["ansible-playbook", "exercise2.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "ok: [nxos1] => (item=1)" in std_out
    assert "ok: [nxos1] => (item=2)" in std_out
    assert "ok: [nxos1] => (item=3)" in std_out
    assert "ok: [nxos1] => (item=4)" in std_out
    assert "4    VLAN0004                         active" in std_out
    assert (
        "nxos1                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class3_ex3():
    base_path = "../class3/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "cisco1                     : ok=5    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert (
        "cisco2                     : ok=5    changed=0    unreachable=0    failed=0    skipped=0"
        in std_out
    )
    assert (
        "ok: [cisco2] => (item=twb-sf-hpsw1        Fa4            120        B               13)"
        in std_out
    )
    assert (
        "ok: [cisco1] => (item=twb-sf-hpsw1        Fa4            120        B               15)"
        in std_out
    )
    assert "Remote device: twb-sf-hpsw1" in std_out
    assert "Local intf: Fa4" in std_out
    assert "Remote intf: 15" in std_out
    assert "Remote intf: 13" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class3_ex4():
    base_path = "../class3/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "arista5                    : ok=1    changed=0" in std_out
    assert "arista6                    : ok=1    changed=0" in std_out
    assert "arista7                    : ok=1    changed=0" in std_out
    assert "arista8                    : ok=1    changed=0" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class3_ex5():
    base_path = "../class3/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "TASK [Generate interface configuration]" in std_out
    assert "TASK [Generate BGP configuration]" in std_out
    assert "TASK [Assemble the two parts into one configuration change file]" in std_out
    assert "nxos1                      : ok=3    changed=0" in std_out
    assert "nxos2                      : ok=3    changed=0" in std_out
    assert std_err == ""
    assert return_code == 0

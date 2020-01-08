import os
import subprocess


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def test_class3_ex1a():
    base_path = "../class3/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1a.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "arista5                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2" in std_out
    assert "arista6                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2" in std_out
    assert "arista7                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2" in std_out
    assert "arista8                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2" in std_out
    assert "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    skipped=3" in std_out
    assert "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    skipped=3" in std_out
    assert "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    skipped=3" in std_out
    assert "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    skipped=3" in std_out
    assert "srx1                       : ok=1    changed=0    unreachable=0    failed=0    skipped=3" in std_out
    assert std_err == ""
    assert return_code == 0

def test_class3_ex1b_eos():
    base_path = "../class3/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1b.yml", "--tags", "eos"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "arista5                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0" in std_out
    assert "arista6                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0" in std_out
    assert "arista7                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0" in std_out
    assert "arista8                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0" in std_out
    assert std_err == ""
    assert return_code == 0

def test_class3_ex1b_ios():
    base_path = "../class3/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1b.yml", "--tags", "ios"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0" in std_out
    assert "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0" in std_out
    assert "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0" in std_out
    assert "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0" in std_out
    assert std_err == ""
    assert return_code == 0

def test_class3_ex1b_junos():
    base_path = "../class3/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1b.yml", "--tags", "junos"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "srx1                       : ok=1    changed=0    unreachable=0    failed=0    skipped=0" in std_out
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
    assert "nxos1                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0" in std_out 
    assert std_err == ""
    assert return_code == 0

import re
import pytest
from pathlib import Path
from utilities import subprocess_runner, remove_ansible_warnings

TEST_CASES = [
    "../class6/collateral/roles_test/test_pb1.yml",
    "../class6/collateral/roles_test/test_pb2.yml",
    "../class6/collateral/roles_test/test_pb3.yml",
    "../class6/collateral/roles_test/test_pb4.yml",
    "../class6/collateral/roles_test/test_pb5.yml",
    "../class6/collateral/tasks/include_import_tags.yml",
    "../class6/collateral/tasks/include_import_when.yml",
    "../class6/collateral/tasks/include_tasks_loop.yml",
    "../class6/collateral/tasks/standalone_pb.yml",
    "../class6/collateral/tasks/standalone_pb2.yml",
    "../class6/collateral/tasks/standalone_pb3.yml",
    # Expected to fail
    # "../class6/collateral/tasks/standalone_pb4.yml",
    "../class6/collateral/vars/test_vars1.yml",
    "../class6/collateral/vars/test_vars2.yml",
    "../class6/collateral/vars/test_vars3.yml",
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


@pytest.mark.parametrize("exercise", ["exercise1a.yml", "exercise1b.yml"])
def test_class6_ex1a_1b(exercise):
    base_path = "../class6/exercises/exercise1"
    cmd_list = ["ansible-playbook", exercise]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert "localhost                  : ok=9" in std_out


@pytest.mark.parametrize(
    "tags,result",
    [(None, "ok=13"), ("foo1", "ok=5"), ("foo2", "ok=5"), ("foo3", "ok=5")],
)
def test_class6_ex1c(tags, result):
    base_path = "../class6/exercises/exercise1"
    if tags:
        cmd_list = ["ansible-playbook", "exercise1c.yml", "--tags", tags]
    else:
        cmd_list = ["ansible-playbook", "exercise1c.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert result in std_out


@pytest.mark.parametrize("exercise", ["exercise2a.yml", "exercise2b.yml"])
def test_class6_ex2a_2b(exercise):
    base_path = "../class6/exercises/exercise2"
    cmd_list = ["ansible-playbook", exercise]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert "localhost                  : ok=2" in std_out


@pytest.mark.parametrize(
    "tags,result",
    [(None, "ok=4"), ("foo1", "ok=2"), ("foo2", "ok=2"), ("foo3", "ok=2")],
)
def test_class6_ex2c(tags, result):
    base_path = "../class6/exercises/exercise2"
    if tags:
        cmd_list = ["ansible-playbook", "exercise2c.yml", "--tags", tags]
    else:
        cmd_list = ["ansible-playbook", "exercise2c.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert result in std_out


def test_class6_ex3():
    """Should be idempotent on the second execution."""
    base_path = "../class6/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    # Execute script again
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"^cisco1\s+:\s+ok=2.*skipped=1.*$", std_out, flags=re.M)
    assert re.search(r"^cisco2\s+:\s+ok=2.*skipped=1.*$", std_out, flags=re.M)
    assert re.search(r"^cisco5\s+:\s+ok=2.*skipped=1.*$", std_out, flags=re.M)
    assert re.search(r"^cisco6\s+:\s+ok=2.*skipped=1.*$", std_out, flags=re.M)


def test_class6_ex4():
    """Should be idempotent on the second execution."""
    base_path = "../class6/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yml", "-f 12"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    # Execute script again
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"^cisco1\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)
    assert re.search(r"^cisco2\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)
    assert re.search(r"^cisco5\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)
    assert re.search(r"^cisco6\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)
    assert re.search(r"^arista5\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)
    assert re.search(r"^arista6\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)
    assert re.search(r"^arista7\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)
    assert re.search(r"^arista8\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)
    assert re.search(r"^nxos1\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)
    assert re.search(r"^nxos2\s+:\s+ok=2.*skipped=3.*$", std_out, flags=re.M)


def test_class6_ex5():
    """Should be idempotent on the second execution."""
    base_path = "../class6/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5.yml", "-f 12"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    # Execute script again
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"^cisco1\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)
    assert re.search(r"^cisco2\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)
    assert re.search(r"^cisco5\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)
    assert re.search(r"^cisco6\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)
    assert re.search(r"^arista5\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)
    assert re.search(r"^arista6\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)
    assert re.search(r"^arista7\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)
    assert re.search(r"^arista8\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)
    assert re.search(r"^nxos1\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)
    assert re.search(r"^nxos2\s+:\s+ok=2.*skipped=2.*$", std_out, flags=re.M)


def test_class6_ex6():
    base_path = "../class6/exercises/exercise6"
    cmd_list = ["ansible-playbook", "exercise6.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0
    assert re.search(r"^cisco5\s+:\s+ok=1 ", std_out, flags=re.M)
    assert re.search(r"^cisco6\s+:\s+ok=1 ", std_out, flags=re.M)

import pytest
from pathlib import Path
from utilities import subprocess_runner, remove_ansible_warnings

TEST_CASES = [
    "../class1/collateral/playbook_structure/simple_pb.yml",
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


def test_class1_ex1a():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1a.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "['rtr1', 701, 3356, '10.1.1.100', '192.168.200.17']" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class1_ex1b():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1b.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "['rtr1', 701, 3356, '10.1.1.100', '192.168.200.17']" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class1_ex1c():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1c.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "rtr1" in std_out
    assert "device_type" in std_out
    assert "cisco1.lasthop.io" in std_out
    assert "password" in std_out
    assert "use_session_log" in std_out
    assert "username" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class1_ex1d():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1d.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "rtr1" in std_out
    assert "device_type" in std_out
    assert "cisco1.lasthop.io" in std_out
    assert "password" in std_out
    assert "use_session_log" in std_out
    assert "username" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class1_ex1e():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1e.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "network_devices" in std_out
    assert std_out.count("cisco_ios") == 2
    assert std_out.count("ip_addresses") == 2
    assert std_out.count("password") == 2
    assert std_err == ""
    assert return_code == 0


def test_class1_ex2a():
    base_path = "../class1/exercises/exercise2/exercise2a"
    cmd_list = ["ansible-inventory", "-i", "inventory.ini", "--list"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        """{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "arista",
            "cisco",
            "local",
            "ungrouped"
        ]
    }
}"""
        in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex2b():
    base_path = "../class1/exercises/exercise2/exercise2b"
    cmd_list = ["ansible-inventory", "-i", "inventory.ini", "--graph"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        """@all:
  |--@arista:
  |  |--arista5
  |  |--arista6
  |--@cisco:
  |  |--cisco1
  |  |--cisco2
  |--@local:
  |--@ungrouped:"""
        in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex2c():
    base_path = "../class1/exercises/exercise2/exercise2c"
    cmd_list = ["ansible-inventory", "-i", "inventory.ini", "--list"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        """            "cisco2": {
                "ansible_connection": "network_cli",
                "ansible_host": "cisco2.lasthop.io",
                "ansible_network_os": "ios",
                "ansible_python_interpreter": "~/VENV/py3_venv/bin/python",
                "ansible_ssh_pass": "bogus",
                "ansible_user": "pyclass"
            }"""
        in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex3a():
    base_path = "../class1/exercises/exercise3"
    cmd_list = ["ansible-playbook", "-i", "inventory.ini", "exercise3a.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "localhost                  : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex3b():
    base_path = "../class1/exercises/exercise3"
    cmd_list = ["ansible-playbook", "-i", "inventory.ini", "exercise3b.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "localhost                  : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex3c():
    base_path = "../class1/exercises/exercise3"
    cmd_list = ["ansible-playbook", "-i", "inventory.ini", "exercise3c.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "cisco1                     : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco2                     : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "localhost                  : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0

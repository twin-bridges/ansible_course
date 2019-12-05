import subprocess


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def test_class1_ex1a():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1a.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "['thingone', 2, 3, 'thingfour', 'lastthing']" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class1_ex1b():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1b.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "['thingone', 2, 3, 'thingfour', 'lastthing']" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class1_ex1c():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1c.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "{'my_dictionary': {'averyfinekey': 'areasonablyokvalue', 'alistkey': ['someelement', "
        "'anotherelement'], 'somebool': False}}" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex1d():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1d.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "{'my_dictionary': {'averyfinekey': 'areasonablyokvalue', 'alistkey': ['someelement', "
        "'anotherelement'], 'somebool': False}}" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex1e():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1e.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "{'combining_data_types': [{'nested_dict': {'really_nested_key': 'reallynestedvalue', "
        "'another_list': [1, 'two'], 'another_nested_dict': {'withinterestingkeys': "
        "'andverycoolvalues'}}}]}" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex1f():
    base_path = "../class1/exercises/exercise1"
    cmd_list = ["python", "print_yaml.py", "exercise1f.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert r"['1042', '{This is a dictionary thingy!}', '\\athing', 'True']" in std_out
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
    cmd_list = ["ansible-playbook", "-i", "inventory.ini", "exercise3a.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "localhost                  : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex3b():
    base_path = "../class1/exercises/exercise3"
    cmd_list = ["ansible-playbook", "-i", "inventory.ini", "exercise3b.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert (
        "localhost                  : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex3c():
    base_path = "../class1/exercises/exercise3"
    cmd_list = ["ansible-playbook", "-i", "inventory.ini", "exercise3c.yaml"]

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

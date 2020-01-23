import os
import subprocess


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def test_class4_ex1():
    base_path = "../class4/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0

def test_class4_ex2():
    base_path = "../class4/exercises/exercise2"
    cmd_list = ["ansible-playbook", "exercise2.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0

def test_class4_ex3():
    base_path = "../class4/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0

def test_class4_ex4():
    base_path = "../class4/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0

def test_class4_ex5():
    # Deprecated module will generate an ansible warning on std_err (disable that)
    os.environ["ANSIBLE_DEPRECATION_WARNINGS"] = "False"
    base_path = "../class4/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_err == ""
    assert return_code == 0
    os.environ.pop("ANSIBLE_DEPRECATION_WARNINGS")

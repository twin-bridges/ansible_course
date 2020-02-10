import subprocess
import re


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


def test_class5_ex1():

    base_path = "../class5/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml", "-f 12"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)

    assert "TASK [IOS global config]" in std_out
    assert "TASK [IOS-XE global config]" in std_out
    assert "TASK [EOS global config]" in std_out
    assert "TASK [NX-OS global config]" in std_out
    assert "TASK [Juniper global config]" in std_out
    for device in [
        "cisco1",
        "cisco2",
        "cisco5",
        "cisco6",
        "arista5",
        "arista6",
        "arista7",
        "arista8",
        "nxos1",
        "nxos2",
    ]:
        assert std_out.count(device) == 6
    for device in ["srx1"]:
        assert std_out.count(device) == 2

    assert std_err == ""
    assert return_code == 0


def test_class5_ex1_idempotent():
    """Run test again to verify idempotency."""
    base_path = "../class5/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1.yml", "-f 12"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    for device in [
        "cisco1",
        "cisco2",
        "cisco5",
        "cisco6",
        "arista5",
        "arista6",
        "arista7",
        "arista8",
        "nxos1",
        "nxos2",
        "srx1",
    ]:
        pattern = rf"^{device}.*changed=0 .*$"
        assert re.search(pattern, std_out, flags=re.M)


def test_class5_ex2():
    base_path = "../class5/exercises/exercise2"
    cmd_list = ["ansible-playbook", "exercise2.yml", "-f 12"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0

    # Should be idempotent as would have been configured in exercise1.
    for device in [
        "cisco1",
        "cisco2",
        "cisco5",
        "cisco6",
        "arista5",
        "arista6",
        "arista7",
        "arista8",
        "nxos1",
        "nxos2",
        "srx1",
    ]:
        pattern = rf"^{device}.*changed=0 .*$"
        assert re.search(pattern, std_out, flags=re.M)


def test_class5_ex3a():
    base_path = "../class5/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3a.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_out.count("permit") == 20
    assert std_err == ""
    assert return_code == 0


def test_class5_ex3b():
    base_path = "../class5/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3b.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_out.count("permit") == 18
    assert std_out.count("deny") == 2
    assert std_err == ""
    assert return_code == 0


def test_class5_ex4():
    base_path = "../class5/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yml"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert "TASK [Generate interface configuration]" in std_out
    assert "TASK [Generate BGP configuration]" in std_out
    assert "TASK [Assemble the two parts into one configuration change file]" in std_out
    assert "TASK [Deploy configurations to devices]" in std_out
    assert "BGP router identifier 172.31.101.101, local AS number 22" in std_out
    assert "BGP router identifier 172.31.101.102, local AS number 22" in std_out
    assert std_err == ""
    assert return_code == 0


def test_class5_ex5():
    base_path = "../class5/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5.yml", "-i", "./ansible-hosts.ini"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    std_err = remove_ansible_warnings(std_err)
    assert std_out.count("student1") == 2
    assert std_err == ""
    assert return_code == 0

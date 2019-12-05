import os
import subprocess


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def test_class2_ex1a():
    base_path = "../class2/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1a.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert (
        "arista5                    : ok=3    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == "[WARNING]: Ignoring timeout(10) for eos_facts\n"
    assert return_code == 0


def test_class2_ex1b():
    base_path = "../class2/exercises/exercise1"
    cmd_list = ["ansible-playbook", "exercise1b.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert "\"ansible_host\": \"arista5.lasthop.io\"" in std_out
    assert (
        "arista5                    : ok=5    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == "[WARNING]: Ignoring timeout(10) for eos_facts\n"
    assert return_code == 0


def test_class2_ex1c():
    base_path = "../class2/exercises/exercise1/exercise1c"
    cmd_list = ["ansible-playbook", "exercise1c.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert "\"ansible_host\": \"arista5.lasthop.io\"" in std_out
    assert "\"ansible_network_os\": \"eos\"" in std_out
    assert "\"ansible_host\": \"arista5.lasthop.io\"" in std_out
    assert "\"desired_eos_version\": \"4.18.3\""
    assert (
        "arista5                    : ok=6    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == "[WARNING]: Ignoring timeout(10) for eos_facts\n"
    assert return_code == 0


def test_class2_ex1d():
    base_path = "../class2/exercises/exercise1/exercise1d"
    cmd_list = ["ansible-playbook", "exercise1d.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert "\"ansible_host\": \"arista5.lasthop.io\"" in std_out
    assert "\"ansible_network_os\": \"eos\"" in std_out
    assert "\"ansible_host\": \"arista5.lasthop.io\"" in std_out
    assert "\"desired_eos_version\": \"4.21.1\""
    assert (
        "arista5                    : ok=6    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == "[WARNING]: Ignoring timeout(10) for eos_facts\n"
    assert return_code == 0


def test_class2_ex1e():
    base_path = "../class2/exercises/exercise1/exercise1e"
    cmd_list = ["ansible-playbook", "exercise1e.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert "\"ansible_host\": \"arista5.lasthop.io\"" in std_out
    assert "\"ansible_network_os\": \"eos\"" in std_out
    assert "\"ansible_host\": \"arista5.lasthop.io\"" in std_out
    assert "\"desired_eos_version\": \"4.21.1\""
    assert "\"device_hostname\": \"arista5.lab.io\""
    assert (
        "arista5                    : ok=8    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == "[WARNING]: Ignoring timeout(10) for eos_facts\n"
    assert return_code == 0


def test_class2_ex2a():
    base_path = "../class2/exercises/exercise2/exercise2a"
    cmd_list = ["ansible-playbook", "exercise2a.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "The ASN for host cisco1 is 65001" in std_out
    assert "The ASN for host cisco2 is 65001" in std_out
    assert "The ASN for host cisco5 is 65001" in std_out
    assert "The ASN for host cisco6 is 65001" in std_out
    assert (
        "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex2b():
    base_path = "../class2/exercises/exercise2/exercise2b"
    cmd_list = ["ansible-playbook", "exercise2b.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "The ASN for host cisco1 is 65001" in std_out
    assert "The ASN for host cisco2 is 65001" in std_out
    assert "The ASN for host cisco5 is 65535" in std_out
    assert "The ASN for host cisco6 is 65001" in std_out
    assert (
        "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex2c():
    base_path = "../class2/exercises/exercise2/exercise2c"
    cmd_list = ["ansible-playbook", "exercise2c.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "The ASN for host cisco1 is 65001, the router-id is 1.1.1.1" in std_out
    assert "The ASN for host cisco2 is 65001, the router-id is 2.2.2.2" in std_out
    assert "The ASN for host cisco5 is 65535, the router-id is 5.5.5.5" in std_out
    assert "The ASN for host cisco6 is 65001, the router-id is 6.6.6.6" in std_out
    assert (
        "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex3a():
    base_path = "../class2/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3a.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("\" NXOS: version 9.2(3)\",") == 2
    assert (
        "nxos1                      : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "nxos2                      : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex3b():
    base_path = "../class2/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3b.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("\" NXOS: version 9.2(3)\",") == 2
    assert std_out.count("\"Flags: * - Adjacencies learnt on non-active FHRP router\"") == 2
    assert (
        "nxos1                      : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "nxos2                      : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex3c():
    base_path = "../class2/exercises/exercise3"
    cmd_list = ["ansible-playbook", "exercise3c.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("Total entries displayed: 4") == 2
    assert (
        "nxos1                      : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "nxos2                      : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex3d():
    base_path = "../class2/exercises/exercise3/exercise3d"
    cmd_list = ["ansible-playbook", "exercise3d.yaml", "-e", f"ansible_ssh_pass={os.environ['ANSIBLE_PASSWORD']}"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("Total entries displayed: 4") == 2
    assert (
        "nxos1                      : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "nxos2                      : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex4a():
    base_path = "../class2/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4.yaml", "-e", f"ansible_ssh_pass={os.environ['ANSIBLE_PASSWORD']}"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("Clear logging buffer [confirm]") == 2
    assert (
        "cisco6                     : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex5a():
    base_path = "../class2/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5a.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "vlan.0                  up    up   inet     10.220.88.39/24" in std_out
    assert (
        "srx1                       : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex5b():
    base_path = "../class2/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5b.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "vlan.0                  up    up   inet     10.220.88.39/24" in std_out
    assert "\"msg\": \"Primary IP: 10.220.88.39/24\"" in std_out
    assert (
        "srx1                       : ok=3    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex5c():
    base_path = "../class2/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5c.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "vlan.0                  up    up   inet     10.220.88.39/24" in std_out
    assert "\"msg\": \"Primary IP: 10.220.88.39/24\"" in std_out
    assert "\"msg\": \"Vlan.0 Interface: vlan.0                  up    up   inet     10.220.88.39/24\"" in std_out
    assert (
        "srx1                       : ok=4    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex5d():
    base_path = "../class2/exercises/exercise5"
    cmd_list = ["ansible-playbook", "exercise5d.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "vlan.0                  up    up   inet     10.220.88.39/24" in std_out
    assert "\"msg\": \"Primary IP: 10.220.88.39/24\"" in std_out
    assert "\"msg\": \"Vlan.0 Interface: vlan.0                  up    up   inet     10.220.88.39/24\"" in std_out
    assert "\"msg\": \"Vlan.0 IP: 10.220.88.39/24\"" in std_out
    assert (
        "srx1                       : ok=5    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex6a():
    base_path = "../class2/exercises/exercise6"
    cmd_list = ["ansible-playbook", "exercise6a.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("Address         Age (min)  Hardware Addr   Interface") == 8
    assert (
        "arista5                    : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "arista6                    : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "arista7                    : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "arista8                    : ok=2    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class2_ex6b():
    base_path = "../class2/exercises/exercise6"
    cmd_list = ["ansible-playbook", "exercise6b.yaml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("\"dynamicEntries\": 5,") == 8
    assert (
        "arista5                    : ok=4    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "arista6                    : ok=4    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "arista7                    : ok=4    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "arista8                    : ok=4    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0

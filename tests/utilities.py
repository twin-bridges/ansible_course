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

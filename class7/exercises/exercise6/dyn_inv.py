#!/usr/bin/env python
"""
Ansible dynamic inventory experimentation
Output dynamic inventory as JSON from statically defined data structures
"""
import argparse
import json

ANSIBLE_INV = {
    "all": {
        "vars": {
            "ansible_connection": "network_cli",
            "ansible_python_interpreter": "/home/student5/VENV/ansible/bin/python",
            "ansible_user": "pyclass",
        },
    },
    "arista": {
        "hosts": ["arista5", "arista6", "arista7", "arista8"],
        "vars": {"ansible_network_os": "eos"},
    },
    "cisco": {
        "hosts": ["cisco1", "cisco2", "cisco5", "cisco6"],
        "vars": {"ansible_network_os": "ios"},
    },
    "juniper": {
        "hosts": ["vmx1", "vmx2"],
        "vars": {"ansible_network_os": "junos", "ansible_connection": "netconf"},
    },
    "nxos": {"hosts": ["nxos1", "nxos2"], "vars": {"ansible_network_os": "nxos"}},
    "local": {"hosts": ["localhost"], "vars": {"ansible_connection": "local"}},
}


HOST_VARS = {
    "arista5": {"ansible_host": "arista5.lasthop.io"},
    "arista6": {"ansible_host": "arista6.lasthop.io"},
    "arista7": {"ansible_host": "arista7.lasthop.io"},
    "arista8": {"ansible_host": "arista8.lasthop.io"},
    "cisco1": {"ansible_host": "cisco1.lasthop.io"},
    "cisco2": {"ansible_host": "cisco2.lasthop.io"},
    "cisco5": {"ansible_host": "cisco5.lasthop.io"},
    "cisco6": {"ansible_host": "cisco6.lasthop.io"},
    "vmx1": {"ansible_host": "vmx1.lasthop.io"},
    "vmx2": {"ansible_host": "vmx2.lasthop.io"},
    "nxos1": {"ansible_host": "nxos1.lasthop.io"},
    "nxos2": {"ansible_host": "nxos2.lasthop.io"},
}


def output_list_inventory(json_output):
    """
    Output the --list data structure as JSON
    """
    print(json.dumps(json_output, indent=4))


def find_host(search_host, inventory):
    """
    Find the given variables for the given host and output them as JSON
    """
    host_attribs = inventory.get(search_host, {})
    print(json.dumps(host_attribs, indent=4))


def main():
    """
    Ansible dynamic inventory experimentation
    Output dynamic inventory as JSON from statically defined data structures
    """

    # Argument parsing
    parser = argparse.ArgumentParser(description="Ansible dynamic inventory")
    parser.add_argument(
        "--list",
        help="Ansible inventory of all of the groups",
        action="store_true",
        dest="list_inventory",
    )
    parser.add_argument(
        "--host",
        help="Ansible inventory of a particular host",
        action="store",
        dest="ansible_host",
        type=str,
    )
    cli_args = parser.parse_args()
    list_inventory = cli_args.list_inventory
    ansible_host = cli_args.ansible_host
    if list_inventory:
        output_list_inventory(ANSIBLE_INV)
    if ansible_host:
        find_host(ansible_host, HOST_VARS)


if __name__ == "__main__":
    main()

"""
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.0.2.15       YES DHCP   up                    up
GigabitEthernet2       unassigned      YES unset  up                    up
GigabitEthernet3       unassigned      YES unset  up                    up
GigabitEthernet4       unassigned      YES unset  up                    up
GigabitEthernet5       unassigned      YES unset  up                    up
GigabitEthernet6       unassigned      YES unset  up                    up
GigabitEthernet7       unassigned      YES unset  up                    up
"""
import re


def show_ip(output):
    show_version_list = []
    output = output.strip()
    for line in output.splitlines():
        if re.search(r"^Interface.*Protocol$", line, flags=re.M):
            continue
        show_version_list.append(line.split())
    return show_version_list


class FilterModule(object):
    def filters(self):
        return {"show_ip_filter": show_ip}

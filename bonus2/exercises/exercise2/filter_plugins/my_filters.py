"""
Reference output from an Arista switch
----------------
Address         Age (min)  Hardware Addr   Interface
10.220.88.1           N/A  0062.ec29.70fe  Vlan1, Ethernet1
10.220.88.28          N/A  00aa.fc05.b513  Vlan1, not learned
10.220.88.29          N/A  00af.fc9a.e49e  Vlan1, not learned
10.220.88.37          N/A  0001.00ff.0001  Vlan1, Ethernet1
10.220.88.38          N/A  0002.00ff.0001  Vlan1, Ethernet1
"""
import re


def show_ip_arp(output):
    arp_list = []
    output = output.strip()
    for line in output.splitlines():
        if re.search(r"^Address.*Interface$", line, flags=re.M):
            continue
        mac_address = line.split()[2]
        arp_list.append(mac_address)

    return arp_list


class FilterModule(object):
    def filters(self):
        return {"show_ip_arp": show_ip_arp}

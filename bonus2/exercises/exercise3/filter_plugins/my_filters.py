"""
Reference output from a Cisco router
----------------
Internet  10.220.88.1            17   0062.ec29.70fe  ARPA   FastEthernet4
Internet  10.220.88.20            -   c89c.1dea.0eb6  ARPA   FastEthernet4
Internet  10.220.88.22          185   a093.5141.b780  ARPA   FastEthernet4
Internet  10.220.88.33          144   00aa.655d.e8c3  ARPA   FastEthernet4
Internet  10.220.88.34          180   00aa.7867.8f6b  ARPA   FastEthernet4
Internet  10.220.88.35          229   00aa.877d.c6e5  ARPA   FastEthernet4
Internet  10.220.88.37           97   0001.00ff.0001  ARPA   FastEthernet4
Internet  10.220.88.38           99   0002.00ff.0001  ARPA   FastEthernet4
"""
import re


def arp_dict(output):
    arp_dict = {}
    output = output.strip()
    for line in output.splitlines():
        if re.search(r".*Address.*Interface$", line, flags=re.M):
            continue
        ip_address = line.split()[1]
        mac_address = line.split()[3]
        arp_dict[ip_address] = mac_address

    return arp_dict


class FilterModule(object):
    def filters(self):
        return {"arp_dict": arp_dict}

""" gets the subnet maskes from CRID notation  """
import sys
from ipaddress import IPv4Interface

if len(sys.argv) > 1:
    filename = sys.argv[1]
    """ else:
    filename = "cidr.txt" """

    with open(filename, 'r') as file:
        for address in file:
            interface = IPv4Interface(address.strip().replace('?', ''))
            print(interface.with_netmask)

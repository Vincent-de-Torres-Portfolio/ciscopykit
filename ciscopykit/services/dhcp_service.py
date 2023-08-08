"""
dhcp_server.py - Module for configuring DHCP and helper addresses in CiscoPyKit.

This module provides functions to configure DHCP settings and add helper addresses
to router interfaces in CiscoPyKit. The `config_dhcp` function allows users to generate
DHCP configuration commands, and the `add_helper_address` function generates commands
to add a helper address to a router interface.

Functions:
    config_dhcp(dhcp_pool_name, network_address, dns_address=None, dg=None, exclude_ips=None):
        Generate DHCP configuration commands.
    
    add_helper_address(interface, helper_address):
        Generate commands to add a helper address to a router interface.

Usage Example:
    ```
    from dhcp_server import config_dhcp, add_helper_address

    dhcp_config = config_dhcp(dhcp_pool_name="V10", network_address="10.3.28.0/22", dns_address="10.3.20.100",
                              exclude_ips=("10.3.30.1", "10.3.30.100"))
    print(dhcp_config)

    helper_config = add_helper_address(interface="FastEthernet0/1", helper_address="10.1.1.2")
    print(helper_config)
    ```

This module provides a simple implementation to generate DHCP configuration and helper address commands
for Cisco routers. Users can use these functions as part of larger network automation workflows.
"""

from ipaddress import IPv4Address, IPv4Network


def config_dhcp(dhcp_pool_name, network_address, dns_address=None, dg=None, exclude_ips=None):
    """
    Configures DHCP on a network.

    BY DEFAULT WILL EXCLUDE THE FIRST 100 USABLE HOST IPS AND SUBNET'S FIRST USABLE ADDRESS AS DG AND THE 10th as DNS
    IF NOT DEFINED: DEFAULT GATEWAY: FIRST USABLE HOST ADDRESS

    :param dhcp_pool_name: str
    :param network_address: str
    :param dns_address: str
    :param dg: str
    :param exclude_ips: tuple
    :return: str
    """
    net_address = IPv4Network(network_address)

    if dg is None:
        dhcp_default_gateway = net_address[1]
    else:
        dhcp_default_gateway = dg

    if exclude_ips is None:
        dhcp_excluded_min = net_address[1]
        dhcp_excluded_max = net_address[100]
    else:
        dhcp_excluded_min = IPv4Address(exclude_ips[0])
        dhcp_excluded_max = IPv4Address(exclude_ips[1])

    if dns_address is None:
        dns_address = net_address[10]

    dhcp_pool_name = dhcp_pool_name
    dhcp_network = net_address

    config = f"""
ip dhcp excluded-address {dhcp_excluded_min} {dhcp_excluded_max}
ip dhcp pool {dhcp_pool_name}
network {dhcp_network.network_address} {dhcp_network.netmask}
default-router {dhcp_default_gateway}
dns-server {dns_address}
exit"""

    return config


def add_helper_address(interface, helper_address):
    """
    Adds a helper address to a router interface.

    :param interface: str
    :param helper_address: str
    :return: str
    """
    config = f"""
interface {interface}
ip helper-address {helper_address}
exit"""
    return config

# if __name__ == "__main__":
#     dhcp_config = config_dhcp(dhcp_pool_name="V10", network_address="10.3.28.0/22", dns_address="10.3.20.100",
#                               exclude_ips=("10.3.30.1", "10.3.30.100"))
#     print(dhcp_config)

#     helper_config = add_helper_address(interface="FastEthernet0/1", helper_address="10.1.1.2")
#     print(helper_config)

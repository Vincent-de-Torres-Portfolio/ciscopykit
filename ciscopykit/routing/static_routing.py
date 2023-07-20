"""
static_routes.py

This module provides functions to configure static routes 
and route redistribution for Cisco devices.

Functions:
- configure_static_route(destination, next_hop, administrative_distance=1): 
Configures a static route on the device.
- configure_default_route(next_hop, exit_interface): Configures a default route on the device.
- configure_route_redistribution(source_protocol, destination_protocol): 
Configures route redistribution between routing protocols.
- generate_static_route_config(destination, next_hop, administrative_distance=1): 
Generates the configuration commands for a static route.
"""
import ipaddress

def configure_static_route(destination, next_hop, administrative_distance=1):
    """
    Generate the configuration command for a static route.

    Args:
        destination (str): The destination network address in CIDR notation (e.g., '10.10.10.0/24').
        next_hop (str): The IP address of the next hop.
        administrative_distance (int, optional): The administrative distance for the static route. Default is 1.

    Returns:
        str: Configuration command for the static route.
    """
    network_address = ipaddress.IPv4Network(destination)
    netmask = str(network_address.netmask)
    next_hop = str(next_hop)
    administrative_distance = int(administrative_distance)

    command = f"ip route {network_address.network_address} {netmask} {next_hop} {administrative_distance}"
    return command
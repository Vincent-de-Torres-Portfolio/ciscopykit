"""
static_routes.py

This module provides functions to configure static routes 
and route redistribution for Cisco devices.

Functions:
- configure_static_route(destination, next_hop, administrative_distance=1): Configures a static route on the device.
- configure_default_route(next_hop, exit_interface): Configures a default route on the device.
- configure_route_redistribution(source_protocol, destination_protocol): Configures route redistribution between routing protocols.
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


def configure_default_route(next_hop):
    """
    Configures a default static route on the Cisco IOS device.

    Args:
        next_hop (str or ipaddress.IPv4Address): The next-hop IP address or exit interface for the default static route.
        exit_interface (str): The exit interface for the default static route.

    Returns:
        str: The configuration command for adding the default static route.

    Raises:
        ValueError: If the next_hop is not a valid IPv4 address.
    """
    try:
        next_hop = ipaddress.IPv4Address(next_hop)
    except ipaddress.AddressValueError:
        raise ValueError("Invalid IPv4 address.")

    command = f"ip route 0.0.0.0 0.0.0.0 {next_hop}"
    return command


def configure_route_redistribution(source_protocol, ospf_id=None, eigrp_as=None):
    """
    Generate Cisco IOS configuration for route redistribution.

    This function generates the configuration commands required to redistribute
    routes from one routing protocol to another in a Cisco IOS device.

    Args:
        source_protocol (str): The source routing protocol from which routes
                               will be redistributed. Supported values are:
                               'static', 'rip', 'eigrp', 'ospf'.
        ospf_id (int, optional): The OSPF process ID if the source_protocol is 'ospf'.
        eigrp_as (int, optional): The EIGRP AS number if the source_protocol is 'eigrp'.

    Returns:
        str: The configuration commands for route redistribution.

    Raises:
        ValueError: If source_protocol is not a supported routing protocol.
                    If ospf_id or eigrp_as is specified for an unsupported protocol.

    Example:
        source_protocol = "static"
        config = configure_route_redistribution(source_protocol)
        print(config)

        source_protocol = "ospf"
        ospf_id = 1
        config = configure_route_redistribution(source_protocol, ospf_id=ospf_id)
        print(config)

        source_protocol = "eigrp"
        eigrp_as = 100
        config = configure_route_redistribution(source_protocol, eigrp_as=eigrp_as)
        print(config)
    """

    supported_source_protocols = {'static', 'rip', 'eigrp', 'ospf'}

    # Validate input protocol
    source_protocol = source_protocol.lower()
    if source_protocol not in supported_source_protocols:
        raise ValueError(
            f"Invalid source_protocol '{source_protocol}'. Supported protocols are: static, rip, eigrp, ospf.")

    if source_protocol == 'ospf' and ospf_id is None:
        raise ValueError(
            "ospf_id must be specified when source_protocol is 'ospf'.")

    if source_protocol == 'eigrp' and eigrp_as is None:
        raise ValueError(
            "eigrp_as must be specified when source_protocol is 'eigrp'.")

    # Generate configuration based on the protocol
    if source_protocol == 'static':
        redistribution_config = """
router eigrp 1
redistribute static
"""
    elif source_protocol == 'ospf':
        redistribution_config = f"""
router ospf {ospf_id}
redistribute connected
"""
    else:
        redistribution_config = f"""
router {source_protocol}
redistribute connected
"""

    return redistribution_config



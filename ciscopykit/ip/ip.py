"""
ip.py - Module for managing IP addresses in CiscoPyKit.

This module provides functions for performing VLSM (Variable Length Subnet Masking)
and subnetting on IPv4 networks.

Functions:
    vlsm(network, new_prefixes): Performs VLSM on an IPv4 network.
    subnet(network, subnet_count): Performs subnetting on an IPv4 network.

Usage Example (for vlsm):
    ```
    # Import the vlsm function from ip.py
    from ip import vlsm

    # Perform VLSM on an IPv4 network
    network = "192.168.0.0/24"
    new_prefixes = [26, 28, 29]
    subnets = vlsm(network, new_prefixes)
    print(subnets)
    ```

Output:
    ```
    [IPv4Network('192.168.0.0/26'), IPv4Network('192.168.0.64/28'), IPv4Network('192.168.0.80/29')]
    ```
"""

import ipaddress

def vlsm(network: str, new_prefixes: list) -> list:
    """
    Performs VLSM (Variable Length Subnet Masking) on an IPv4 network.

    Args:
        network (str): The IPv4 network in the format "x.x.x.x/y".
        new_prefixes (list): The list of new prefix lengths for each subnet in the network.

    Returns:
        list: The list of subnets created by the VLSM process.

    Raises:
        ValueError: If the provided network or prefix lengths are invalid.
    """
    try:
        network = ipaddress.IPv4Network(network)
    except ipaddress.AddressValueError:
        raise ValueError("Invalid IPv4 network format.")

    if not all(isinstance(prefix, int) and 1 <= prefix <= 32 for prefix in new_prefixes):
        raise ValueError("Invalid prefix length. Prefix length must be an integer between 1 and 32.")

    new_prefixes.sort(reverse=True)
    subnets = []

    for prefix in new_prefixes:
        if network.prefixlen > prefix:
            raise ValueError("New prefix length must be larger than the original network prefix length.")
        to_add = list(network.subnets(new_prefix=prefix))
        subnets.extend(to_add)
        network = to_add[-1]

    return subnets

def subnet(network: str, subnet_count: int) -> list:
    """
    Performs subnetting on an IPv4 network.

    Args:
        network (str): The IPv4 network in the format "x.x.x.x/y".
        subnet_count (int): The number of subnets to create.

    Returns:
        list: The list of subnets created by the subnetting process.

    Raises:
        ValueError: If the provided network or subnet count is invalid.
    """
    try:
        network = ipaddress.IPv4Network(network)
    except ipaddress.AddressValueError:
        raise ValueError("Invalid IPv4 network format.")

    if not isinstance(subnet_count, int) or subnet_count <= 0:
        raise ValueError("Invalid subnet count. Subnet count must be a positive integer.")

    pref_diff = subnet_count.bit_length()
    if network.prefixlen + pref_diff > 32:
        raise ValueError("The specified subnet count exceeds the maximum possible subnets.")

    nextworks = list(network.subnets(prefixlen_diff=pref_diff))
    return [net for net in nextworks]

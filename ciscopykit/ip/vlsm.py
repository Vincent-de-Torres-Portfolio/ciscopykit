"""
vlsm.py - Subpackage for performing Variable Length Subnet Masking (VLSM) and subnetting in CiscoPyKit.

This subpackage provides functions to perform Variable Length Subnet Masking (VLSM) and subnetting
on IPv4 networks in CiscoPyKit. The `vlsm` function allows users to perform VLSM on a given IPv4
network, creating subnets with custom prefix lengths. The `subnet` function performs regular subnetting
on an IPv4 network, dividing it into a specified number of subnets.

Functions:
    vlsm(network: str, new_prefixes: List[int]) -> List[ipaddress.IPv4Network]:
        Performs Variable Length Subnet Masking (VLSM) on an IPv4 network.

    subnet(network: str, subnet_count: int) -> List[ipaddress.IPv4Network]:
        Performs subnetting on an IPv4 network.

Usage Example:
    ```
    # Import the functions from vlsm.py
    from ciscopykit.vlsm import vlsm, subnet

    # Perform VLSM on an IPv4 network
    network = "192.168.1.0/24"
    new_prefixes = [26, 28, 30]
    subnets_vlsm = vlsm(network, new_prefixes)
    print(subnets_vlsm)

    # Perform subnetting on an IPv4 network
    network = "10.0.0.0/8"
    subnet_count = 16
    subnets_subnet = subnet(network, subnet_count)
    print(subnets_subnet)
    ```

Output:
    ```
    [IPv4Network('192.168.1.0/26'), IPv4Network('192.168.1.64/28'), IPv4Network('192.168.1.80/30')]
    [IPv4Network('10.0.0.0/16'), IPv4Network('10.0.1.0/16'), IPv4Network('10.0.2.0/16'), ...]
    ```

This subpackage provides a simple implementation of VLSM and subnetting for IPv4 networks. Users can
customize the prefix lengths for each subnet or specify the number of subnets they want to create.
"""

import argparse
from ipaddress import IPv4Network
from math import log2
from typing import List

def vlsm(network: IPv4Network, new_prefixes: List[int]) -> List[IPv4Network]:
    """
    Performs VLSM (Variable Length Subnet Masking) on an IPv4 network.

    Args:
        network (IPv4Network): The IPv4 network in the format 'x.x.x.x/y'.
        new_prefixes (List[int]): The list of new prefix lengths for each subnet in the network.

    Returns:
        List[IPv4Network]: The list of subnets created by the VLSM process.

    Raises:
        ValueError: If the new_prefixes list is empty.
        ValueError: If any of the new prefixes is not greater than the original prefix.
        ValueError: If any of the new prefixes is greater than 32 or less than the original prefix.
    """
    if not new_prefixes:
        raise ValueError("The new_prefixes list cannot be empty.")

    if not all(new_prefix > network.prefixlen for new_prefix in new_prefixes):
        raise ValueError("All new prefixes must be greater than the original prefix length.")

    if any(new_prefix > 32 or new_prefix < network.prefixlen for new_prefix in new_prefixes):
        raise ValueError("New prefix lengths must be between the original prefix length and 32.")

    subnets = []
    new_prefixes.sort()

    subnet_list = network.subnets(new_prefix=new_prefixes[0])
    subnets.append(subnet_list.__next__())
    new_prefixes.pop(0)

    for each_netmask in new_prefixes:
        next_subnet = subnet_list.__next__()
        to_add = next_subnet.subnets(new_prefix=each_netmask)
        subnets.append(to_add.__next__())

    return subnets

def subnet(network: IPv4Network, subnet_count: int) -> List[IPv4Network]:
    """
    Performs subnetting on an IPv4 network.

    Args:
        network (IPv4Network): The IPv4 network in the format 'x.x.x.x/y'.
        subnet_count (int): The number of subnets to create.

    Returns:
        List[IPv4Network]: The list of subnets created by the subnetting process.

    Raises:
        ValueError: If the subnet_count is not a positive integer.
        ValueError: If the subnet_count is greater than 2^p where p is the prefix length of the original network.
    """
    if not isinstance(subnet_count, int) or subnet_count <= 0:
        raise ValueError("The subnet_count must be a positive integer.")

    max_subnets = 2 ** (32 - network.prefixlen)
    if subnet_count > max_subnets:
        raise ValueError(f"The subnet_count cannot be greater than {max_subnets} for this network.")

    subnets = []
    pref_diff = log2(subnet_count).__ceil__()
    nextworks = network.subnets(prefixlen_diff=pref_diff)
    subnets.extend(nextworks)

    return subnets

def parse_args():
    """
    Parses command-line arguments for the VLSM and subnetting operations.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Perform VLSM or subnetting on an IPv4 network.")
    parser.add_argument("network", type=IPv4Network, help="IPv4 network in the format 'x.x.x.x/y'")
    parser.add_argument("operation", choices=["vlsm", "subnet"], help="VLSM or subnet operation")
    parser.add_argument("--new-prefixes", type=int, nargs="+", help="New prefix lengths for VLSM")
    parser.add_argument("--subnet-count", type=int, help="Number of subnets for subnetting")
    return parser.parse_args()

def main():
    """
    Main function to perform VLSM or subnetting based on command-line arguments.
    """
    args = parse_args()

    if args.operation == "vlsm":
        if not args.new_prefixes:
            raise ValueError("For VLSM, new-prefixes argument is required.")
        result = vlsm(args.network, args.new_prefixes)
    else:
        if not args.subnet_count:
            raise ValueError("For subnetting, subnet-count argument is required.")
        result = subnet(args.network, args.subnet_count)

    for subnet in result:
        print(subnet)

if __name__ == "__main__":
    main()

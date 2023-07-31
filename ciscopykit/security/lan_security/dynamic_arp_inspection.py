"""
LAN Security Package

The LAN Security package provides a collection of modules and functions that 
assist in configuring various security features and settings for local area networks
(LANs).These security measures are designed to protect network infrastructure, 
prevent unauthorized access, and mitigate potential security risks.

Module: stp_security

This module provides functions to configure Spanning Tree Protocol (STP) 
security features such as PortFast and BPDU Guard.

Functions:
- configure_portfast_default(): Configures PortFast on all access ports by default.
- configure_bpdu_guard(interface): Configures BPDU Guard on the specified interface.
- configure_stp_security(interface): Configures PortFast and BPDU Guard on the specified interface.

Module: dai_security

This module provides functions to configure Dynamic ARP Inspection (DAI) security feature.

Functions:
- generate_dai_config(interfaces, vlan=None): Configures Dynamic ARP Inspection (DAI) 
on the specified interfaces and VLAN.

Main Script: app.py

The app.py script is a command-line tool that utilizes the functions from the 
stp_security and dai_security modules to generate configuration commands for 
LAN security features. It supports configuring STP security (PortFast and BPDU Guard)
and DAI security (Dynamic ARP Inspection).

Usage: python app.py [--interface INTERFACE] [--security {stp,dai}] [--vlan VLAN_ID]

Arguments:
  --interface INTERFACE     Interface name.
  --security {stp,dai}      Security feature to configure (stp or dai).
  --vlan VLAN_ID            VLAN ID for DAI configuration (optional).

Example Usage:
- Configure STP security:
    python app.py --interface GigabitEthernet1/0/1 --security stp

- Configure DAI security:
    python app.py --interface GigabitEthernet1/0/1 --security dai --vlan 10
"""


def generate_dai_config(interfaces, vlan=None):
    """
    Configures Dynamic ARP Inspection (DAI) on the specified interfaces and VLAN.

    Args:
        interfaces (list): A list of interfaces on which to enable DAI.
        vlan (int or None, optional): The VLAN ID for which to enable DAI. 
        If not specified or set to None, DAI will be enabled on all VLANs.

    Returns:
        str: The configuration commands for enabling DAI on the interfaces and VLAN.

    Raises:
        ValueError: If the interface name is not valid.
        ValueError: If the VLAN ID is not a positive integer.
    """

    valid_interface_types = [
        "GigabitEthernet", "FastEthernet", "Ethernet", "Serial", "Portchannel", "VLAN", "Gi", "G", "Fa", "F", "Se", "S", "Po"]
    commands = []

    if vlan is not None and not all(isinstance(each, int) and each > 0 for each in vlan):
        raise ValueError(
            "Invalid VLAN ID. The VLAN ID must be a positive integer.")

    for interface in interfaces:
        interface_type = interface.split()[0]

        if interface_type not in valid_interface_types:
            raise ValueError(
                f"Invalid interface name. The interface type must be one of: {', '.join(valid_interface_types)}"
            )

        command = f"interface {interface}\n"
        command += "ip arp inspection trust\n"

    if vlan is not None:
        vlan_ids = ",".join(str(v) for v in vlan)
        command += f"ip arp inspection vlan {vlan_ids}\n"

        commands.append(command)

    return "\n".join(commands)

# print(generate_dai_config(['Gi 0/0'],[1,2,3,4]))

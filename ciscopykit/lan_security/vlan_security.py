"""
Module: vlan_security

This module provides functions to configure VLAN security features.

Functions:
- configure_trunk_interfaces(interface_range): Configures trunk interfaces with non-negotiating trunks and assigns them to a default VLAN.
- configure_unused_ports(interface_range, unused_vlan): Configures unused ports as access ports, assigns them to a specified VLAN, and shuts down the ports.
- configure_access_ports(interface_range): Configures access ports to prevent trunking.

Usage: 

# Configure trunk interfaces
trunk_interfaces = "fa0/1 - 4"
trunk_config = configure_trunk_interfaces(trunk_interfaces)
print(trunk_config)

# Configure unused ports
unused_ports = "fa0/5 - 10"
unused_vlan = 86
unused_config = configure_unused_ports(unused_ports, unused_vlan)
print(unused_config)

# Configure access ports
access_ports = "fa0/11 - 24"
access_config = configure_access_ports(access_ports)
print(access_config)
"""


def configure_trunk_interfaces(interface_range):
    """
    Configures trunk interfaces with non-negotiating trunks and assigns them to a default VLAN.

    Args:
        interface_range (str): Range of interfaces in the format "fa0/1 - 4".

    Returns:
        str: The configuration commands for configuring the trunk interfaces.

    """
    command = f"interface range {interface_range}"
    command += "\nswitchport mode trunk"
    command += "\nswitchport nonegotiate"
    command += "\nswitchport trunk native vlan 99"

    return command


def configure_unused_ports(interface_range, unused_vlan):
    """
    Configures unused ports as access ports, assigns them to a specified VLAN, and shuts down the ports.

    Args:
        interface_range (str): Range of interfaces in the format "fa0/5 - 10".
        unused_vlan (int): VLAN ID for the unused ports.

    Returns:
        str: The configuration commands for configuring the unused ports.

    """
    command = f"interface range {interface_range}"
    command += "\nswitchport mode access"
    command += f"\nswitchport access vlan {unused_vlan}"
    command += "\nshutdown"

    return command


def configure_access_ports(interface_range):
    """
    Configures access ports to prevent trunking.

    Args:
        interface_range (str): Range of interfaces in the format "fa0/11 - 24".

    Returns:
        str: The configuration commands for configuring the access ports.

    """
    command = f"interface range {interface_range}"
    command += "\nswitchport mode access"

    return command


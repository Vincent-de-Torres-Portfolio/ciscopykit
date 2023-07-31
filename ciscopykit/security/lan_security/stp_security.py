"""
Module: stp_security

This module provides functions to configure Spanning Tree Protocol (STP) security features such as PortFast and BPDU Guard.

Functions:
- configure_portfast_default(): Configures PortFast on all access ports by default.
- configure_bpdu_guard(interface): Configures BPDU Guard on the specified interface.
- configure_stp_security(interface): Configures PortFast and BPDU Guard on the specified interface.

Raises:
- ValueError: If the interface name is not valid.
"""


def configure_portfast_default():
    """
    Configures PortFast on all access ports by default.

    Returns:
        str: The configuration command for enabling PortFast by default.
    """
    command = "spanning-tree portfast default"
    return command


def configure_bpdu_guard(interface):
    """
    Configures BPDU Guard on the specified interface.

    Args:
        interface (str): The interface name on which to enable BPDU Guard.

    Returns:
        str: The configuration command for enabling BPDU Guard on the interface.

    Raises:
        ValueError: If the interface name is not valid.
    """
    valid_interface_types = [
        "GigabitEthernet", "FastEthernet", "Ethernet", "Serial", "Portchannel", "VLAN"]
    interface_type = interface.split()[0]

    if interface_type not in valid_interface_types:
        raise ValueError(
            f"Invalid interface name. The interface type must be one of: {', '.join(valid_interface_types)}"
        )

    command = f"interface {interface}\n"
    command += "spanning-tree bpduguard enable"
    return command


def configure_stp_security(interface):
    """
    Configures PortFast and BPDU Guard on the specified interface.

    Args:
        interface (str): The interface name on which to configure PortFast and BPDU Guard.

    Returns:
        str: The configuration commands for enabling PortFast and BPDU Guard on the interface.

    Raises:
        ValueError: If the interface name is not valid.
    """
    valid_interface_types = [
        "GigabitEthernet", "FastEthernet", "Ethernet", "Serial", "Portchannel", "VLAN"]
    interface_type = interface.split()[0]

    if interface_type not in valid_interface_types:
        raise ValueError(
            f"Invalid interface name. The interface type must be one of: {', '.join(valid_interface_types)}"
        )

    portfast_command = configure_portfast_default()
    bpdu_guard_command = configure_bpdu_guard(interface)
    commands = f"{portfast_command}\n{bpdu_guard_command}"
    return commands

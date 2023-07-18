"""
Module: switchport_security

This module provides a function to generate the configuration command for switchport security.

Function:
- generate_switchport_security_config(interface, max_mac, violation_action='restrict', aging_time=None, sticky_mac=True):
    Generates the configuration command for switchport security.

    Args:
        interface (str): Interface name.
        max_mac (int): Maximum number of MAC addresses to be learned.
        violation_action (str, optional): Violation action. Can be 'restrict', 'protect', or 'shutdown'. (default: 'restrict')
        aging_time (int, optional): Aging time for dynamically learned secure MAC addresses in minutes. (default: None)
        sticky_mac (bool, optional): Whether to enable sticky MAC address. (default: True)

    Returns:
        str: Configuration command for switchport security.

    Raises:
        ValueError: If the violation action is not one of 'restrict', 'protect', or 'shutdown'.
"""


def generate_switchport_security_config(interface, max_mac, violation_action='restrict', aging_time=None, sticky_mac=True):
    """
    Generate the configuration command for switchport security.

    Args:
        interface (str): Interface name.
        max_mac (int): Maximum number of MAC addresses to be learned.
        violation_action (str, optional): Violation action. Can be 'restrict', 'protect', or 'shutdown'. (default: 'restrict')
        aging_time (int, optional): Aging time for dynamically learned secure MAC addresses in minutes. (default: None)
        sticky_mac (bool, optional): Whether to enable sticky MAC address. (default: True)

    Returns:
        str: Configuration command for switchport security.

    Raises:
        ValueError: If the violation action is not one of 'restrict', 'protect', or 'shutdown'.
    """
    if violation_action not in ['restrict', 'protect', 'shutdown']:
        raise ValueError(
            "Invalid violation action. It must be 'restrict', 'protect', or 'shutdown'.")

    command = f"interface {interface}\n"
    command += " switchport mode access\n"
    command += " switchport port-security\n"
    command += f" switchport port-security maximum {max_mac}\n"
    command += f" switchport port-security violation {violation_action}\n"

    if aging_time is not None:
        command += f" switchport port-security aging time {aging_time}\n"

    if sticky_mac:
        command += " switchport port-security mac-address sticky\n"

    return command

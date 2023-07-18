"""
Module: dhcp_snooping

This module provides a function to generate a DHCP snooping configuration for an IOS device.

Function:
- generate_dhcp_snooping_config(interface, trust_ports): Generates a DHCP snooping configuration for an IOS device.

Args:
- interface (str): The interface on which DHCP snooping should be enabled.
- trust_ports (list): A list of interfaces that should be trusted by DHCP snooping.

Returns:
- str: The DHCP snooping configuration that can be copied and pasted onto an IOS device.

Raises:
- ValueError: If interface or trust_ports are not provided.

Usage:
    interface = 'GigabitEthernet0/1'
    trust_ports = ['GigabitEthernet0/2', 'GigabitEthernet0/3']
    dhcp_snooping_config = generate_dhcp_snooping_config(interface, trust_ports)
    print(dhcp_snooping_config)

"""

def generate_dhcp_snooping_config(interface, trust_ports):
    """
    Generates a DHCP snooping configuration for an IOS device.

    Args:
        interface (str): The interface on which DHCP snooping should be enabled.
        trust_ports (list): A list of interfaces that should be trusted by DHCP snooping.

    Returns:
        str: The DHCP snooping configuration that can be copied and pasted onto an IOS device.

    Raises:
        ValueError: If interface or trust_ports are not provided.

    """
    # Validate the input
    if not interface:
        raise ValueError("Interface must be specified.")
    if not trust_ports:
        raise ValueError("At least one trust port must be specified.")

    config_lines = []

    # Enable DHCP snooping globally
    config_lines.append('ip dhcp snooping')

    # Enable DHCP snooping trust on the specified interface
    config_lines.append(f'interface {interface}')
    config_lines.append('  ip dhcp snooping trust')

    # Enable DHCP snooping trust on the specified trust ports
    for port in trust_ports:
        config_lines.append(f'interface {port}')
        config_lines.append('  ip dhcp snooping trust')

    # Combine the configuration lines into a single string
    config = '\n'.join(config_lines)

    return config

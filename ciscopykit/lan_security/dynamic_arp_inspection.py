def generate_dai_config(interfaces):
    """
    Generates a Dynamic ARP Inspection (DAI) configuration for an IOS device.

    Args:
        interfaces (list): A list of interfaces on which DAI should be enabled.

    Returns:
        str: The DAI configuration that can be copied and pasted onto an IOS device.

    Raises:
        ValueError: If interfaces are not provided.
    
    Sample Usage:
        interfaces = ['GigabitEthernet0/1', 'GigabitEthernet0/2', 'GigabitEthernet0/3']

        dai_config = generate_dai_config(interfaces)
        print(dai_config)
        
    Sample Output:
        ip arp inspection
        !
        interface GigabitEthernet0/1
        ip arp inspection trust
        !
        interface GigabitEthernet0/2
        ip arp inspection trust
        !
        interface GigabitEthernet0/3
        ip arp inspection trust
    """
    
    # Validate the input
    if not interfaces:
        raise ValueError("At least one interface must be specified.")

    config_lines = []

    # Enable DAI globally
    config_lines.append('ip arp inspection')

    # Enable DAI trust on the specified interfaces
    for interface in interfaces:
        config_lines.append(f'interface {interface}')
        config_lines.append('  ip arp inspection trust')

    # Combine the configuration lines into a single string
    config = '\n'.join(config_lines)

    return config

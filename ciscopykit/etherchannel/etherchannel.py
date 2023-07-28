"""
etherchannel.py - A module for configuring Layer 2 and Layer 3 EtherChannels in CiscoPyKit.

This module provides classes for configuring and generating EtherChannel configurations for
both Layer 2 and Layer 3 EtherChannels. The classes in this module are designed to serve as a
template for implementing different types of EtherChannels in CiscoPyKit.

Classes:
    EtherChannel: Base class for configuring EtherChannels.
    Layer2EtherChannel: Class representing a Layer 2 EtherChannel configuration.
    Layer3EtherChannel: Class representing a Layer 3 EtherChannel configuration.

Attributes:
    (None)

Usage:
    To use this module, import the classes and create instances of the Layer2EtherChannel and
    Layer3EtherChannel classes with the required parameters. Then, call the 'configure()' method
    on the instances to get the configuration commands for the respective EtherChannel type.

Example:
    ```
    from etherchannel import Layer2EtherChannel, Layer3EtherChannel

    # Example configuration for Layer 2 EtherChannel
    interfaces = ["GigabitEthernet0/1", "GigabitEthernet0/2"]
    l2_etherchannel = Layer2EtherChannel(port_channel_number=1, interfaces=interfaces)
    l2_config = l2_etherchannel.configure()
    print(l2_config)

    # Example configuration for Layer 3 EtherChannel
    interfaces = ["GigabitEthernet0/3", "GigabitEthernet0/4"]
    ip_address = "192.168.1.1"
    subnet_mask = "255.255.255.0"
    l3_etherchannel = Layer3EtherChannel(port_channel_number=2, interfaces=interfaces, ip_address=ip_address, subnet_mask=subnet_mask)
    l3_config = l3_etherchannel.configure()
    print(l3_config)
    ```
"""
import ipaddress
import re
class EtherChannel:
    """
    Base class for configuring EtherChannels.

    This class serves as a template for implementing different types of EtherChannels
    in CiscoPyKit.

    Attributes:
        port_channel_number (int): The number of the port-channel interface.

    Methods:
        configure(): Abstract method to configure the EtherChannel.
            Subclasses must implement this method.

    Raises:
        NotImplementedError: Raised when 'configure' method is not implemented
            by the subclass.
    """

    def __init__(self, port_channel_number):
        """
        Initialize an EtherChannel.

        Args:
            port_channel_number (int): The number of the port-channel interface.
        """
        self.port_channel_number = port_channel_number

    def configure(self):
        """
        Abstract method to configure the EtherChannel.

        Subclasses must implement this method.

        Raises:
            NotImplementedError: Raised when the method is not implemented by the subclass.
        """
        raise NotImplementedError("Subclasses must implement the 'configure' method.")
    

class Layer2EtherChannel(EtherChannel):
    """
    Class representing a Layer 2 EtherChannel configuration.

    Layer 2 EtherChannel is used to bundle multiple physical interfaces
    into a single logical interface without IP addressing.

    Attributes:
        port_channel_number (int): The number of the port-channel interface.
        interfaces (list): List of physical interfaces to be bundled.
        allowed_vlans (str): Optional. VLANs allowed on the trunk interface.

    Methods:
        configure(): Configures the Layer 2 EtherChannel.

    Raises:
        ValueError: If the port_channel_number is not in the valid range (1 to 4096).
        ValueError: If there are not enough interfaces (minimum 2) to form the EtherChannel.
        ValueError: If the allowed_vlans string format is invalid.
    """

    def __init__(self, port_channel_number, interfaces, allowed_vlans=None):
        super().__init__(port_channel_number)

        if not (1 <= port_channel_number <= 4096):
            raise ValueError("Invalid port channel number. The number must be in the range 1 to 4096.")

        if len(interfaces) < 2:
            raise ValueError("Layer 2 EtherChannel requires at least 2 interfaces to form the bundle.")

        self.interfaces = interfaces

        if allowed_vlans is not None:
            # Validate the format of allowed_vlans (e.g., "1,2,3" or "1-5,10,20")
            if not re.match(r'^\d+(-\d+)?(,\d+(-\d+)?)*$', allowed_vlans):
                raise ValueError("Invalid format for allowed_vlans. Use comma-separated VLAN numbers "
                                 "or VLAN ranges (e.g., '1,2,3' or '1-5,10,20').")

            self.allowed_vlans = allowed_vlans
        else:
            self.allowed_vlans = None

    def configure(self):
        """
        Configure Layer 2 EtherChannel.

        Returns:
            str: The configuration commands for configuring the Layer 2 EtherChannel.
        """
        config_commands = [
            f"interface range {', '.join(self.interfaces)}",
            f"channel-group {self.port_channel_number} mode active",
            f"exit",
            f"interface port-channel {self.port_channel_number}"
        ]

        if self.allowed_vlans:
            config_commands.extend([
                f"switchport mode trunk",
                f"switchport trunk allowed vlan {self.allowed_vlans}"
            ])

        return "\n".join(config_commands)

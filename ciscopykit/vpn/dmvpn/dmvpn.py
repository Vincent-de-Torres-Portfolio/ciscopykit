"""
dmvpn.py - Module for configuring DMVPN (Dynamic Multipoint Virtual Private Network) hubs and spokes in CiscoPyKit.

This module provides classes to represent and configure DMVPN hubs and spokes in CiscoPyKit.
The DMVPNHub and DMVPNSpoke classes allow users to create DMVPN hub and spoke configurations.

Classes:
    DMVPNHub: Class representing a DMVPN hub configuration.
    DMVPNSpoke: Class representing a DMVPN spoke configuration.

Methods:
    configure(): Generate the configuration for the DMVPN hub or spoke.

Usage Example:
    ```
    # Import the DMVPNHub and DMVPNSpoke classes from dmvpn.py
    from dmvpn import DMVPNHub, DMVPNSpoke

    # Create a DMVPN hub configuration
    hub = DMVPNHub(
        tunnel_interface="Tunnel0",
        hub_ip="10.0.0.1",
        nhrp_group="dmvpn_group",
        nhrp_authentication="cisco123"
    )
    hub_config = hub.configure()

    print(hub_config)

    # Create a DMVPN spoke configuration
    spoke = DMVPNSpoke(
        tunnel_interface="Tunnel0",
        spoke_ip="192.168.1.1",
        hub_ip="10.0.0.1",
        nhrp_group="dmvpn_group",
        nhrp_authentication="cisco123"
    )
    spoke_config = spoke.configure()

    print(spoke_config)
    ```
"""

class DMVPNHub:
    """
    Class representing a DMVPN hub configuration.

    Attributes:
        tunnel_interface (str): The name of the tunnel interface.
        hub_ip (str): The IP address of the hub.
        nhrp_group (str): The NHRP group name.
        nhrp_authentication (str): The NHRP authentication string.

    Methods:
        configure(): Generate the configuration for the DMVPN hub.

    Returns:
        str: The configuration commands for the DMVPN hub.
    """

    def __init__(self, tunnel_interface, hub_ip, nhrp_group, nhrp_authentication):
        """
        Initialize a DMVPN hub configuration.

        Args:
            tunnel_interface (str): The name of the tunnel interface.
            hub_ip (str): The IP address of the hub.
            nhrp_group (str): The NHRP group name.
            nhrp_authentication (str): The NHRP authentication string.
        """
        self.tunnel_interface = tunnel_interface
        self.hub_ip = hub_ip
        self.nhrp_group = nhrp_group
        self.nhrp_authentication = nhrp_authentication

    def configure(self):
        """
        Generate the configuration for the DMVPN hub.

        Returns:
            str: The configuration commands for the DMVPN hub.
        """
        config = f"""
interface {self.tunnel_interface}
ip address {self.hub_ip}
tunnel mode gre multipoint
ip nhrp group {self.nhrp_group}
ip nhrp authentication {self.nhrp_authentication}
"""
        return config.strip()

class DMVPNSpoke:
    """
    Class representing a DMVPN spoke configuration.

    Attributes:
        tunnel_interface (str): The name of the tunnel interface.
        spoke_ip (str): The IP address of the spoke.
        hub_ip (str): The IP address of the hub.
        nhrp_group (str): The NHRP group name.
        nhrp_authentication (str): The NHRP authentication string.

    Methods:
        configure(): Generate the configuration for the DMVPN spoke.

    Returns:
        str: The configuration commands for the DMVPN spoke.
    """

    def __init__(self, tunnel_interface, spoke_ip, hub_ip, nhrp_group, nhrp_authentication):
        """
        Initialize a DMVPN spoke configuration.

        Args:
            tunnel_interface (str): The name of the tunnel interface.
            spoke_ip (str): The IP address of the spoke.
            hub_ip (str): The IP address of the hub.
            nhrp_group (str): The NHRP group name.
            nhrp_authentication (str): The NHRP authentication string.
        """
        self.tunnel_interface = tunnel_interface
        self.spoke_ip = spoke_ip
        self.hub_ip = hub_ip
        self.nhrp_group = nhrp_group
        self.nhrp_authentication = nhrp_authentication

    def configure(self):
        """
        Generate the configuration for the DMVPN spoke.

        Returns:
            str: The configuration commands for the DMVPN spoke.
        """
        config = f"""
interface {self.tunnel_interface}
ip address {self.spoke_ip}
tunnel mode gre multipoint
tunnel source {self.spoke_ip}
tunnel destination {self.hub_ip}
ip nhrp group {self.nhrp_group}
ip nhrp authentication {self.nhrp_authentication}
"""
        return config.strip()

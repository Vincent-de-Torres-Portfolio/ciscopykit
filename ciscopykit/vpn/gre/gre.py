"""
gre.py - Module for configuring Generic Routing Encapsulation (GRE) tunnels in CiscoPyKit.

This module provides a class to represent and configure GRE tunnels in CiscoPyKit.
The GRE class allows users to create GRE tunnels with various configurations.

Class:
    GRE: Class representing a Generic Routing Encapsulation (GRE) tunnel.

Methods:
    configure(): Generate the configuration for the GRE tunnel.

Usage Example:
    ```
    # Import the GRE class from gre.py
    from gre import GRE

    # Create a GRE tunnel configuration
    tunnel_id = 1
    tunnel_source = "10.0.0.1"
    tunnel_destination = "20.0.0.1"
    tunnel_ip = "192.168.0.1"

    gre_tunnel = GRE(tunnel_id, tunnel_source, tunnel_destination, tunnel_ip)
    gre_config = gre_tunnel.configure()

    print(gre_config)
    ```

Output:
    ```
    interface Tunnel1
    ip address 10.0.0.1 20.0.0.1
    tunnel source 10.0.0.1
    tunnel destination 20.0.0.1
    ip address 192.168.0.1
    ```

"""

import ipaddress
import argparse

class GRE:
    """
    Class representing a Generic Routing Encapsulation (GRE) tunnel configuration.

    Attributes:
        tunnel_id (int): The ID of the GRE tunnel.
        tunnel_source (str): The source IP address of the GRE tunnel.
        tunnel_destination (str): The destination IP address of the GRE tunnel.
        tunnel_ip (str): Optional IP address to assign to the GRE tunnel interface.

    Methods:
        configure(): Generate the configuration for the GRE tunnel.

    Raises:
        ValueError: If the provided tunnel_id is not within the valid range.
        ValueError: If the provided IP addresses are not valid IPv4 addresses.
    """

    def __init__(self, tunnel_id, tunnel_source, tunnel_destination, tunnel_ip=None):
        """
        Initialize a GRE tunnel.

        Args:
            tunnel_id (int): The ID of the GRE tunnel (must be within 1 to 65535).
            tunnel_source (str): The source IP address of the GRE tunnel.
            tunnel_destination (str): The destination IP address of the GRE tunnel.
            tunnel_ip (str, optional): The IP address to assign to the GRE tunnel interface.
        """
        if not (1 <= tunnel_id <= 65535):
            raise ValueError("Invalid tunnel ID. Tunnel ID must be within 1 to 65535.")
        
        try:
            self.tunnel_source = ipaddress.IPv4Address(tunnel_source)
            self.tunnel_destination = ipaddress.IPv4Address(tunnel_destination)
        except ipaddress.AddressValueError:
            raise ValueError("Invalid IP address format.")

        if tunnel_ip:
            try:
                self.tunnel_ip = ipaddress.IPv4Address(tunnel_ip)
            except ipaddress.AddressValueError:
                raise ValueError("Invalid IP address format for tunnel_ip.")
        else:
            self.tunnel_ip = None

        self.tunnel_id = tunnel_id

    def configure(self):
        """
        Generate the configuration for the GRE tunnel.

        Returns:
            str: The configuration commands for the GRE tunnel.
        """
        config = f"""
        interface Tunnel{self.tunnel_id}
        ip address {self.tunnel_source} {self.tunnel_destination}
        tunnel source {self.tunnel_source}
        tunnel destination {self.tunnel_destination}
        """
        if self.tunnel_ip:
            config += f"\n ip address {self.tunnel_ip}"

        return config.strip()


def main():
    parser = argparse.ArgumentParser(description="Configure a Generic Routing Encapsulation (GRE) tunnel.")
    parser.add_argument("tunnel_id", type=int, help="The ID of the GRE tunnel (1 to 65535).")
    parser.add_argument("tunnel_source", type=str, help="The source IP address of the GRE tunnel.")
    parser.add_argument("tunnel_destination", type=str, help="The destination IP address of the GRE tunnel.")
    parser.add_argument("--tunnel_ip", type=str, help="Optional IP address to assign to the GRE tunnel interface.")

    args = parser.parse_args()
    gre_tunnel = GRE(args.tunnel_id, args.tunnel_source, args.tunnel_destination, args.tunnel_ip)
    gre_config = gre_tunnel.configure()

    print(gre_config)

if __name__ == "__main__":
    main()
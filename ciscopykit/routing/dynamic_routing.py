"""
dynamic_routing.py - A module for configuring and generating dynamic routing protocols.

This module provides a framework for configuring and generating configurations
for dynamic routing protocols such as RIP, OSPF, and EIGRP. It uses Object-Oriented
Programming (OOP) to define classes for each protocol, making it easy to extend and
add support for more routing protocols in the future.

Classes:
    DynamicRoutingProtocol: A base class to represent a dynamic routing protocol.
    RIP: A class representing the RIP (Routing Information Protocol) routing protocol.
    OSPF: A class representing the OSPF (Open Shortest Path First) routing protocol.
    EIGRP: A class representing the EIGRP (Enhanced Interior Gateway Routing Protocol) routing protocol.

Usage:
    To use this module, create instances of the routing protocol classes (RIP, OSPF, or EIGRP),
    configure the protocol using the 'configure' method, and generate configurations with the 'generate_config'
    method. Please note that the 'configure' and 'generate_config' methods need to be implemented in the
    subclasses for each specific routing protocol.

Example:
    `RIP : Configure RIP routing protocol`
    
    networks = ["192.168.0.0", "10.0.0.0"]
    passive_interfaces = ["GigabitEthernet0/1", "GigabitEthernet0/2"]

    rip_protocol = RIP(version=2, networks=networks, no_auto_summary=True, passive_interfaces=passive_interfaces)
    rip_config = rip_protocol.generate_config()

    print(rip_config)

"""


class DynamicRoutingProtocol:
    def __init__(self, networks):
        self.networks = networks

    def configure(self):
        raise NotImplementedError("Subclasses must implement the 'configure' method.")

    def generate_config(self):
        raise NotImplementedError("Subclasses must implement the 'generate_config' method.")

class RIP(DynamicRoutingProtocol):
    
    def __init__(self, version, networks, no_auto_summary=False, passive_interfaces=None):
        """
        Initialize a RIP routing protocol.

        Args:
            version (int): The version of RIP to use (1 or 2).
            networks (list): A list of networks to advertise with RIP.
            no_auto_summary (bool, optional): Whether to disable auto-summary (default: False).
            passive_interfaces (list, optional): A list of interfaces to be set as passive (default: None).
        
        Raises:
            ValueError: If the version is not 1 or 2.
        """
        super().__init__(networks)

        if version not in [1, 2]:
            raise ValueError("Invalid RIP version. The version must be 1 or 2.")
        
        self.version = version
        self.no_auto_summary = no_auto_summary
        self.passive_interfaces = passive_interfaces or []

    def configure(self):
        """
        Configure RIP routing protocol on the device.

        Returns:
            str: The configuration commands for configuring RIP.
        """
        # Implementation to configure RIP routing protocol
        rip_config = "router rip\n"
        rip_config += f"version {self.version}\n"
        
        if self.no_auto_summary:
            rip_config += "no auto-summary\n"

        for network in self.networks:
            rip_config += f"network {network}\n"

        for interface in self.passive_interfaces:
            rip_config += f"passive-interface {interface}\n"
        
        return rip_config

    def generate_config(self):
        """
        Generate RIP configuration.

        Returns:
            str: The configuration commands for RIP protocol configuration.
        """
        # Implementation to generate RIP configuration
        return self.configure()


class OSPF(DynamicRoutingProtocol):
    def __init__(self, process_id, network, area):
        super().__init__(network)
        self.process_id = process_id
        self.area = area

    def configure(self):
        # Implementation to configure OSPF routing protocol
        pass

    def generate_config(self):
        # Implementation to generate OSPF configuration
        pass

class EIGRP(DynamicRoutingProtocol):
    def __init__(self, as_number, network):
        super().__init__(network)
        self.as_number = as_number

    def configure(self):
        # Implementation to configure EIGRP routing protocol
        pass

    def generate_config(self):
        # Implementation to generate EIGRP configuration
        pass



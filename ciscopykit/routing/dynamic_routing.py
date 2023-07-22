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
import ipaddress

class DynamicRoutingProtocol:
    """
    Base class for dynamic routing protocols.

    This class serves as a template for implementing dynamic routing protocols in CiscoPyKit.
    Subclasses must implement the 'configure' and 'generate_config' methods to configure the
    respective routing protocols on the device and generate the configuration.

    Attributes:
        networks (list): A list of network addresses to be advertised.

    Methods:
        configure(): Abstract method to configure the dynamic routing protocol on the device.
            Subclasses must implement this method.
        
        generate_config(): Abstract method to generate the configuration for the dynamic routing
            protocol. Subclasses must implement this method.

    Raises:
        NotImplementedError: Raised when 'configure' and 'generate_config' methods are not implemented
            by the subclass.
    """

    def __init__(self, networks):
        """
        Initialize a dynamic routing protocol.

        Args:
            networks (list): A list of network addresses to be advertised.
        """
        self.networks = networks

    def configure(self):
        """
        Abstract method to configure the dynamic routing protocol on the device.

        Subclasses must implement this method.

        Raises:
            NotImplementedError: Raised when the method is not implemented by the subclass.
        """
        raise NotImplementedError("Subclasses must implement the 'configure' method.")

    def generate_config(self):
        """
        Abstract method to generate the configuration for the dynamic routing protocol.

        Subclasses must implement this method.

        Raises:
            NotImplementedError: Raised when the method is not implemented by the subclass.
        """
        raise NotImplementedError("Subclasses must implement the 'generate_config' method.")

class RIP(DynamicRoutingProtocol):
    """
    Class representing the RIP (Routing Information Protocol) routing protocol.

    RIP is a dynamic routing protocol that is widely used in small to medium-sized networks.
    It is a distance-vector protocol and uses hop count as the metric to calculate the best
    path to a destination network.

    Attributes:
        version (int): The version of RIP to use (1 or 2).
        networks (list): A list of networks to advertise with RIP.
        no_auto_summary (bool, optional): Whether to disable auto-summary (default: False).
        passive_interfaces (list, optional): A list of interfaces to be set as passive (default: None).
    
    Methods:
        configure(): Configures the RIP routing protocol on the device.
        generate_config(): Generates the configuration for the RIP routing protocol.

    Raises:
        ValueError: If the version is not 1 or 2.
    """

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

class OSPF(DynamicRoutingProtocol):
    """
    Class representing the OSPF (Open Shortest Path First) routing protocol.

    OSPF is a link-state routing protocol that is widely used in large networks.
    It uses Dijkstra's algorithm to calculate the shortest path to a destination network.

    Attributes:
        process_id (int): The OSPF process ID.
        router_id (str): The OSPF router ID.
        ospf_options (dict, optional): Dictionary containing OSPF-specific options (default: None).

    Raises:
        ValueError: If the process ID is not a positive integer.
        ValueError: If the provided IP addresses are not valid.
    """

    def __init__(self, process_id, router_id, ospf_options=None):
        """
        Initialize an OSPF routing protocol.

        Args:
            process_id (int): The OSPF process ID.
            router_id (str): The OSPF router ID.
            ospf_options (dict, optional): Dictionary containing OSPF-specific options (default: None).

        Raises:
            ValueError: If the process ID is not a positive integer.
        """
        if not isinstance(process_id, int) or process_id <= 0:
            raise ValueError("Invalid OSPF process ID. The process ID must be a positive integer.")

        self.process_id = process_id
        self.router_id = router_id
        self.ospf_options = ospf_options or {}
        self.networks = self.ospf_options.get('networks', [])
        self.passive_interfaces = self.ospf_options.get('passive_interfaces', [])
        self.default_route_interface = self.ospf_options.get('default_route_interface')

    def _validate_ip_addresses(self, ip_addresses):
        for ip in ip_addresses:
            try:
                ipaddress.IPv4Network(ip)
            except ipaddress.AddressValueError:
                raise ValueError(f"Invalid IP address: {ip}")

    def _cidr_to_network(self, cidr):
        ip_net = ipaddress.IPv4Network(cidr)
        return str(ip_net.network_address)

    def configure(self):
        """
        Configure OSPF routing protocol on the device.

        Returns:
            str: The configuration commands for configuring OSPF.
        """
        ospf_config = [f"router ospf {self.process_id}"]
        ospf_config.append(f"router-id {self.router_id}")

        for network in self.networks:
            network_address = self._cidr_to_network(network)
            ospf_config.append(f"network {network_address} 0.0.0.255 area 0")

        for interface in self.passive_interfaces:
            ospf_config.append(f"passive-interface {interface}")

        if self.default_route_interface:
            ospf_config.append(f"default-information originate always metric 1 metric-type 1 {self.default_route_interface}")

        return "\n".join(ospf_config)
    
    def generate_config(self):
        return self.configure()


# Example usage

networks = ["192.168.0.0", "10.0.0.0"]
passive_interfaces = ["GigabitEthernet0/1", "GigabitEthernet0/2"]

rip_protocol = RIP(version=2, networks=networks, no_auto_summary=True, passive_interfaces=passive_interfaces)
rip_config = rip_protocol.generate_config()

print(rip_config)

##################################
# OSPF                          #
#################################
ospf_options = {
    'networks': ['192.168.1.0/24', '10.0.0.0/16'],
    'passive_interfaces': ['GigabitEthernet0/1', 'Serial0/0/0'],
    'default_route': True
}

ospf_instance = OSPF(process_id=10, router_id='6.6.6.6', ospf_options=ospf_options)

# Generate OSPF configuration
ospf_config = ospf_instance.generate_config()

# Print the generated configuration
print(ospf_config)


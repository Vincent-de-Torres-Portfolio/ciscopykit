import re

class Device:
    """
    Represents a network device.

    Attributes:
        device_type (str): The type of the device.
        hostname (str): The hostname of the device.
        site (str): The site name of the device.
        fqdn (str): The fully qualified domain name of the device.
        active_interfaces (list): The list of active interfaces.
        layer (str): The layer of the device (Core, Distribution, Access).

    Methods:
        modify_hostname(new_hostname): Modifies the hostname of the 
device.
        modify_site(new_site): Modifies the site name of the device.
        remove_attribute(attribute_name): Removes an attribute from the 
device.
        add_interface(interface): Adds an interface to the device.
        remove_interface(interface): Removes an interface from the device.
        update_fqdn(): Updates the fully qualified domain name based on 
the hostname and site name.
        extract_hostname_site(fqdn): Extracts the hostname and site name 
from a fully qualified domain name.
        get_active_interfaces(): Returns the list of active interfaces.
    """

    def __init__(self, device_type, hostname, site, layer):
        """
        Initializes a Device object.

        Args:
            device_type (str): The type of the device.
            hostname (str): The hostname of the device.
            site (str): The site name of the device.
            layer (str): The layer of the device (Core, Distribution, 
Access).
        """
        self.device_type = device_type
        self._hostname = hostname
        self._site = site
        self.fqdn = f"{hostname}.{site}"
        self.active_interfaces = []
        self.layer = layer

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, new_hostname):
        self._hostname = new_hostname
        self.update_fqdn()

    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, new_site):
        self._site = new_site
        self.update_fqdn()

    def __str__(self):
        """
        Returns a string representation of the device.

        Returns:
            str: The string representation of the device.
        """
        return f"{self.device_type} ({self.fqdn})"

    def modify_hostname(self, new_hostname):
        """
        Modifies the hostname of the device.

        Args:
            new_hostname (str): The new hostname of the device.
        """
        self.hostname = new_hostname

    def modify_site(self, new_site):
        """
        Modifies the site name of the device.

        Args:
            new_site (str): The new site name of the device.
        """
        self.site = new_site

    def remove_attribute(self, attribute_name):
        """
        Removes an attribute from the device.

        Args:
            attribute_name (str): The name of the attribute to remove.
        """
        if hasattr(self, attribute_name):
            delattr(self, attribute_name)

    def add_interface(self, interface):
        """
        Adds an interface to the device.

        Args:
            interface (Interface): The interface to add.
        """
        self.active_interfaces.append(interface)

    def remove_interface(self, interface):
        """
        Removes an interface from the device.

        Args:
            interface (Interface): The interface to remove.
        """
        if interface in self.active_interfaces:
            self.active_interfaces.remove(interface)

    def update_fqdn(self):
        """
        Updates the fully qualified domain name based on the hostname and 
site name.
        """
        self.fqdn = f"{self.hostname}.{self.site}"

    @staticmethod
    def extract_hostname_site(fqdn):
        """
        Extracts the hostname and site name from a fully qualified domain 
name.

        Args:
            fqdn (str): The fully qualified domain name.

        Returns:
            tuple: A tuple containing the hostname and site name.

        Raises:
            ValueError: If the fully qualified domain name is invalid.
        """
        pattern = r'^(?P<hostname>[^.]+)\.(?P<site>[^.]+)\..+$'
        match = re.match(pattern, fqdn)
        if match:
            hostname = match.group('hostname')
            site = match.group('site')
            return hostname, site
        else:
            raise ValueError("Invalid fully qualified domain name.")

    def get_active_interfaces(self):
        """
        Returns the list of active interfaces.

        Returns:
            list: The list of active interfaces.
        """
        return self.active_interfaces
    @staticmethod
    def generate_init_config(hostname, site, interface_range="GigabitEthernet0/0-10", static_pass="cisco", motd="Welcome to the Cisco network!"):
        """
        Generates the initial configuration for the device.

        Args:
            hostname (str): The hostname to be set in the configuration.
            site (str): The site name to be used in the configuration.
            interface_range (str, optional): The range of interfaces. Defaults to "GigabitEthernet0/0-10".
            static_pass (str, optional): The static password for the device. Defaults to "cisco".
            motd (str, optional): The Message of the Day (MOTD) for the device. Defaults to "Welcome to the Cisco network!".

        Returns:
            str: The generated initial configuration.
        """
        # Generate configuration
        config = f'''
!{'='*40}!
! {hostname}{' ' * (39-len(hostname))}!      
!{'='*40}!  
 
enable
configure terminal
no ip domain-lookup
hostname {hostname}
username admin secret {static_pass}
    
line console 0
logging synchronous
exit
conf t
ip domain-name {site}.ccna.com
crypto key generate rsa
1024
    
banner motd ${motd}$
enable secret {static_pass}
line console 0
password {static_pass}
login
exit
    
line vty 0 4
login local
transport input ssh
ip ssh version 2
    
service password-encryption
'''
        return config

    @staticmethod
    def generate_interface_config(interface_name, ip_address, subnet_mask):
        """
        Generates the interface configuration for a specific interface.

        Args:
            interface_name (str): The name of the interface.
            ip_address (str): The IP address of the interface.
            subnet_mask (str): The subnet mask of the interface.

        Returns:
            str: The generated interface configuration.
        """
        return f"""
interface {interface_name}
no switchport
ip address {ip_address} {subnet_mask}
no shutdown
"""


class Router(Device):
    """
    Represents a router device.
    """

    def __init__(self, hostname, site, layer):
        super().__init__("Router", hostname, site, layer)
    


class L3Switch(Device):
    """
    Represents an L3 switch device.
    """

    def __init__(self, hostname, site, layer):
        super().__init__("L3 Switch", hostname, site, layer)


class L2Switch(Device):
    """
    Represents an L2 switch device.
    """

    def __init__(self, hostname, site, layer):
        super().__init__("L2 Switch", hostname, site, layer)


class Endpoint(Device):
    """
    Represents an endpoint device.
    """

    def __init__(self, hostname, site, layer):
        super().__init__("Endpoint", hostname, site, layer)


class CoreLayer:
    """
    Represents the Core layer in a network.
    """

    def __init__(self):
        self.devices = []

    def add_device(self, device):
        """
        Adds a device to the Core layer.

        Args:
            device (Device): The device to add.
        """
        self.devices.append(device)


class DistributionLayer:
    """
    Represents the Distribution layer in a network.
    """

    def __init__(self):
        self.devices = []

    def add_device(self, device):
        """
        Adds a device to the Distribution layer.

        Args:
            device (Device): The device to add.
        """
        self.devices.append(device)


class AccessLayer:
    """
    Represents the Access layer in a network.
    """

    def __init__(self):
        self.devices = []

    def add_device(self, device):
        """
        Adds a device to the Access layer.

        Args:
            device (Device): The device to add.
        """
        self.devices.append(device)


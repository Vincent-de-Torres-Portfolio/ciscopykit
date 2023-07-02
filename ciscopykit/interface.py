import ipaddress

class Interface:
    """
    Represents a network interface.

    Attributes:
        name (str): The name of the interface.
        ip_address (ipaddress.IPv4Interface or None): The IP address 
assigned to the interface, if any.

    Methods:
        assign_ip_address(ip_address): Assigns an IP address to the 
interface.
        remove_ip_address(): Removes the assigned IP address from the 
interface.
    """

    def __init__(self, name):
        """
        Initializes an Interface object.

        Args:
            name (str): The name of the interface.
        """
        self.name = name
        self.ip_address = None

    def assign_ip_address(self, ip_address):
        """
        Assigns an IP address to the interface.

        Args:
            ip_address (str or ipaddress.IPv4Interface): The IP address to 
assign to the interface.
                It can be a string representing the IP address (e.g., 
'192.168.1.1') or an
                ipaddress.IPv4Interface object.

        Raises:
            ValueError: If the provided IP address is invalid.
        """
        if isinstance(ip_address, str):
            try:
                self.ip_address = ipaddress.IPv4Interface(ip_address)
            except ipaddress.AddressValueError:
                raise ValueError("Invalid IP address.")
        elif isinstance(ip_address, ipaddress.IPv4Interface):
            self.ip_address = ip_address
        else:
            raise TypeError("Invalid IP address format.")

    def remove_ip_address(self):
        """
        Removes the assigned IP address from the interface.
        """
        self.ip_address = None

    def __str__(self):
        """
        Returns a string representation of the interface.

        Returns:
            str: The string representation of the interface.
        """
        return f"Interface: {self.name}"

    def __repr__(self):
        """
        Returns a detailed string representation of the interface.

        Returns:
            str: The detailed string representation of the interface.
        """
        if self.ip_address:
            return f"Interface: {self.name} | IP: {str(self.ip_address)}"
        else:
            return f"Interface: {self.name} | IP: Unassigned"


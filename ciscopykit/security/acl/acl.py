"""
acl.py - Module for configuring Access Control Lists (ACLs) in CiscoPyKit.

This module provides a class to represent and configure Access Control Lists (ACLs)
in CiscoPyKit. The ACL class allows users to create standard numbered ACLs and named ACLs,
and add or remove entries to define traffic filtering rules.

Class:
    ACL: Class representing a standard numbered or named Access Control List (ACL).

Methods:
    add_entry(entry): Add an entry to the ACL.
    remove_entry(entry): Remove an entry from the ACL.
    configure(): Generate the configuration for the ACL.

Usage Example:
    ```
    # Import the ACL class from acl.py
    from acl import ACL

    # Create a standard numbered ACL with number 10
    acl = ACL(acl_number=10)

    # Add entries to the ACL
    acl.add_entry("10 permit 192.168.1.0 0.0.0.255")
    acl.add_entry("20 deny any")

    # Remove an entry from the ACL
    acl.remove_entry("20 deny any")

    # Generate the configuration for the ACL
    acl_config = acl.configure()
    print(acl_config)
    ```

Output:
    ```
    access-list 10 standard
    10 permit 192.168.1.0 0.0.0.255
    ```

Usage Example for Named ACL:
    ```
    # Import the ACL class from acl.py
    from acl import ACL

    # Create a named ACL with name "my_acl"
    acl = ACL(acl_name="my_acl")

    # Add entries to the ACL
    acl.add_entry("permit ip 192.168.1.0 0.0.0.255 any")
    acl.add_entry("deny ip any any")

    # Remove an entry from the ACL
    acl.remove_entry("deny ip any any")

    # Generate the configuration for the ACL
    acl_config = acl.configure()
    print(acl_config)
    ```

Output:
    ```
    ip access-list extended my_acl
    permit ip 192.168.1.0 0.0.0.255 any
    ```
"""

class ACL:
    """
    Class representing a standard numbered or named Access Control List (ACL).

    Attributes:
        acl_number (int): The ACL number (for standard numbered ACLs).
        acl_name (str): The ACL name (for named ACLs).
        entries (list): List of ACL entries.

    Methods:
        add_entry(entry): Add an entry to the ACL.
        remove_entry(entry): Remove an entry from the ACL.
        configure(): Generate the configuration for the ACL.

    Raises:
        ValueError: If an entry with the same sequence number already exists (for numbered ACLs).
    """

    def __init__(self, acl_number=None, acl_name=None):
        """
        Initialize an ACL.

        Args:
            acl_number (int, optional): The ACL number (for standard numbered ACLs).
            acl_name (str, optional): The ACL name (for named ACLs).
        """
        self.acl_number = acl_number
        self.acl_name = acl_name
        self.entries = []

    def add_entry(self, entry):
        """
        Add an entry to the ACL.

        Args:
            entry (str): The ACL entry to add.

        Raises:
            ValueError: If an entry with the same sequence number already exists (for numbered ACLs).
        """
        if self.acl_number is not None:
            for existing_entry in self.entries:
                if existing_entry.split()[0] == entry.split()[0]:
                    raise ValueError("Entry with the same sequence number already exists.")
        self.entries.append(entry)

    def remove_entry(self, entry):
        """
        Remove an entry from the ACL.

        Args:
            entry (str): The ACL entry to remove.
        """
        if entry in self.entries:
            self.entries.remove(entry)

    def configure(self):
        """
        Generate the configuration for the ACL.

        Returns:
            str: The configuration commands for the ACL.
        """
        acl_config = []
        if self.acl_number is not None:
            acl_config.append(f"access-list {self.acl_number} standard")
        elif self.acl_name is not None:
            acl_config.append(f"ip access-list extended {self.acl_name}")
        acl_config.extend(self.entries)
        return "\n".join(acl_config)

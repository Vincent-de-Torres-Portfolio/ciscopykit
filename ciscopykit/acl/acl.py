"""
acl.py - Module for configuring Access Control Lists (ACLs) in CiscoPyKit.

This module provides a class to represent and configure Access Control Lists (ACLs)
in CiscoPyKit. The ACL class allows users to create standard numbered ACLs and add or
remove entries to define traffic filtering rules.

Class:
    ACL: Class representing a standard numbered Access Control List (ACL).

Methods:
    add_entry(entry): Add an entry to the ACL.
    remove_entry(entry): Remove an entry from the ACL.
    configure(): Generate the configuration for the ACL.

Usage Example:
    ```
    # Import the ACL class from acl.py
    from acl import ACL

    # Create an ACL with number 10
    acl = ACL(10)

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

This module provides a simple implementation of a standard numbered ACL that allows users
to add and remove entries to define traffic filtering rules. Users can extend this module
to support other types of ACLs, such as extended numbered ACLs or named ACLs, as needed.
"""

class ACL:
    """
    Class representing a standard numbered Access Control List (ACL).

    Attributes:
        acl_number (int): The ACL number.
        entries (list): List of ACL entries.

    Methods:
        add_entry(entry): Add an entry to the ACL.
        remove_entry(entry): Remove an entry from the ACL.
        configure(): Generate the configuration for the ACL.

    Raises:
        ValueError: If an entry with the same sequence number already exists.
    """

    def __init__(self, acl_number):
        """
        Initialize a standard numbered ACL.

        Args:
            acl_number (int): The ACL number.
        """
        self.acl_number = acl_number
        self.entries = []

    def add_entry(self, entry):
        """
        Add an entry to the ACL.

        Args:
            entry (str): The ACL entry to add.

        Raises:
            ValueError: If an entry with the same sequence number already exists.
        """
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
        acl_config = [f"access-list {self.acl_number} standard"]
        acl_config.extend(self.entries)
        return "\n".join(acl_config)
    


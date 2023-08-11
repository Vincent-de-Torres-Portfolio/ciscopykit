from abc import ABC, abstractmethod

class ACL(ABC):
    """
    Abstract base class representing an Access Control List (ACL).

    Attributes:
        acl_identifier (int or str): The ACL identifier (number or name).
        entries (list): List of ACL entries.

    Methods:
        add_entry(entry): Add an entry to the ACL.
        remove_entry(entry): Remove an entry from the ACL.
        configure(): Generate the configuration for the ACL.

    Raises:
        ValueError: If an entry with the same sequence number already exists (for numbered ACLs).
    """

    def __init__(self, acl_identifier):
        """
        Initialize an ACL.

        Args:
            acl_identifier (int or str): The ACL identifier (number or name).
        """
        self.acl_identifier = acl_identifier
        self.entries = []

    @abstractmethod
    def configure(self):
        """
        Abstract method to generate the configuration for the ACL.

        Subclasses must implement this method.

        Raises:
            NotImplementedError: Raised when the method is not implemented by the subclass.
        """
        pass

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

class StandardNumberedACL(ACL):
    """
    Class representing a standard numbered Access Control List (ACL).

    Methods:
        configure(): Generate the configuration for the standard numbered ACL.
    """

    def __init__(self, acl_number):
        """
        Initialize a standard numbered ACL.

        Args:
            acl_number (int): The ACL number.

        Raises:
            ValueError: If the ACL number is not within the valid range.
        """
        if not (1 <= acl_number <= 99):
            raise ValueError("Invalid ACL number for standard numbered ACL. Must be between 1 and 99.")
        super().__init__(acl_number)

    def configure(self):
        """
        Generate the configuration for the standard numbered ACL.

        Returns:
            str: The configuration commands for the standard numbered ACL.
        """
        acl_config = [f"access-list {self.acl_identifier} standard"]
        acl_config.extend(self.entries)
        return "\n".join(acl_config)

class ExtendedNumberedACL(ACL):
    """
    Class representing an extended numbered Access Control List (ACL).

    Methods:
        configure(): Generate the configuration for the extended numbered ACL.
    """

    def __init__(self, acl_number):
        """
        Initialize an extended numbered ACL.

        Args:
            acl_number (int): The ACL number.

        Raises:
            ValueError: If the ACL number is not within the valid range.
        """
        if not (100 <= acl_number <= 199):
            raise ValueError("Invalid ACL number for extended numbered ACL. Must be between 100 and 199.")
        super().__init__(acl_number)

    def configure(self):
        """
        Generate the configuration for the extended numbered ACL.

        Returns:
            str: The configuration commands for the extended numbered ACL.
        """
        acl_config = [f"access-list {self.acl_identifier} extended"]
        acl_config.extend(self.entries)
        return "\n".join(acl_config)

class NamedStandardACL(ACL):
    """
    Class representing a named standard Access Control List (ACL).

    Methods:
        configure(): Generate the configuration for the named standard ACL.
    """

    def __init__(self, acl_name):
        """
        Initialize a named standard ACL.

        Args:
            acl_name (str): The ACL name.
        """
        super().__init__(acl_name)

    def configure(self):
        """
        Generate the configuration for the named standard ACL.

        Returns:
            str: The configuration commands for the named standard ACL.
        """
        acl_config = [f"ip access-list standard {self.acl_identifier}"]
        acl_config.extend(self.entries)
        return "\n".join(acl_config)

class NamedExtendedACL(ACL):
    """
    Class representing a named extended Access Control List (ACL).

    Methods:
        configure(): Generate the configuration for the named extended ACL.
    """

    def __init__(self, acl_name):
        """
        Initialize a named extended ACL.

        Args:
            acl_name (str): The ACL name.
        """
        super().__init__(acl_name)

    def configure(self):
        """
        Generate the configuration for the named extended ACL.

        Returns:
            str: The configuration commands for the named extended ACL.
        """
        acl_config = [f"ip access-list extended {self.acl_identifier}"]
        acl_config.extend(self.entries)
        return "\n".join(acl_config)

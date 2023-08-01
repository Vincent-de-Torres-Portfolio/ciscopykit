# acl.py - Module for Configuring Access Control Lists (ACLs) in CiscoPyKit

This module provides a class to represent and configure Access Control Lists (ACLs) in CiscoPyKit. The `ACL` class allows users to create standard numbered ACLs and named ACLs and add or remove entries to define traffic filtering rules.

## Class:

### ACL

Class representing a standard numbered or named Access Control List (ACL).

#### Attributes:

- `acl_number` (int): The ACL number (for standard numbered ACLs).
- `acl_name` (str): The ACL name (for named ACLs).
- `entries` (list): List of ACL entries.

#### Methods:

- `add_entry(entry)`: Add an entry to the ACL.
- `remove_entry(entry)`: Remove an entry from the ACL.
- `configure()`: Generate the configuration for the ACL.

#### Raises:

- `ValueError`: If an entry with the same sequence number already exists (for numbered ACLs).

## Usage Example:

```python
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

## Usage Example for Named ACL:

```python
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
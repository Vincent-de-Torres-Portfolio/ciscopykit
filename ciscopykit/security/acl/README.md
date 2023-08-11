# CiscoPyKit ACL Module

The **CiscoPyKit ACL Module** provides a flexible and extensible way to create, manage, and configure Access Control Lists (ACLs) in the CiscoPyKit framework.

## Overview

Access Control Lists (ACLs) are an essential part of network security and traffic filtering. The CiscoPyKit ACL Module allows you to easily define ACLs with different types (standard, extended) and identify them by either numbers or names. You can add and remove entries to these ACLs to define traffic filtering rules.

## Features

- Create standard numbered ACLs with a number between 1 and 99.
- Create extended numbered ACLs with a number between 100 and 199.
- Create named standard ACLs.
- Create named extended ACLs.
- Add and remove entries to define traffic filtering rules.
- Generate configuration commands based on the defined ACLs.

## Usage Examples

### Creating a Standard Numbered ACL

```python
from acl import StandardNumberedACL

# Create a standard numbered ACL with number 10
acl = StandardNumberedACL(acl_number=10)

# Add entries to the ACL
acl.add_entry("10 permit 192.168.1.0 0.0.0.255")
acl.add_entry("20 deny any")

# Generate the configuration for the ACL
acl_config = acl.configure()
print(acl_config)
```

### Creating a Named Extended ACL

```python
from acl import NamedExtendedACL

# Create a named extended ACL with name "my_acl"
acl = NamedExtendedACL(acl_name="my_acl")

# Add entries to the ACL
acl.add_entry("permit ip 192.168.1.0 0.0.0.255 any")
acl.add_entry("deny ip any any")

# Generate the configuration for the ACL
acl_config = acl.configure()
print(acl_config)
```

## Installation

1. Clone the repository or download the `acl.py` module.
2. Include the `acl.py` module in your project.
3. Import the necessary classes from `acl` and start creating and managing ACLs.

## Contributions

Contributions to enhance the CiscoPyKit ACL Module are welcome! Feel free to submit pull requests or open issues for bug reports, feature requests, or general discussions.

## License

This module is released under the [MIT License](LICENSE).

---
# [`ciscopykit`](/)
## Device Module

The `device` module provides classes to represent network devices and 
their interfaces.

### Installation

The `device` module can be installed using pip:

```bash
pip install ciscopykit
```

### Usage

#### Device Class

The `Device` class represents a network device and provides methods to 
modify attributes, add/remove interfaces, and manage the fully qualified 
domain name (FQDN) of the device.

```python
from ciscopykit.device import Device

# Create a new device
device = Device(device_type="Router", hostname="router1", site="site1")

# Modify the hostname and site of the device
device.modify_hostname("router2")
device.modify_site("site2")

# Add an interface to the device
device.add_interface("GigabitEthernet0/1")

# Remove an interface from the device
device.remove_interface("GigabitEthernet0/1")

# Get the list of active interfaces
interfaces = device.get_active_interfaces()

# Print the device details
print(device)
```

#### Interface Class

The `Interface` class represents a network interface and provides methods 
to assign and remove IP addresses.

```python
from ciscopykit.interface import Interface

# Create a new interface
interface = Interface(name="GigabitEthernet0/1")

# Assign an IP address to the interface
interface.assign_ip_address("192.168.1.1")

# Remove the IP address from the interface
interface.remove_ip_address()

# Print the interface details
print(interface)
```

### Documentation

#### Device Class

##### `__init__(device_type, hostname, site)`

* Initializes a Device object.
* Args:
  * `device_type (str)`: The type of the device.
  * `hostname (str)`: The hostname of the device.
  * `site (str)`: The site name of the device.

##### `modify_hostname(new_hostname)`

* Modifies the hostname of the device.
* Args:
  * `new_hostname (str)`: The new hostname of the device.

##### `modify_site(new_site)`

* Modifies the site name of the device.
* Args:
  * `new_site (str)`: The new site name of the device.

##### `remove_attribute(attribute_name)`

* Removes an attribute from the device.
* Args:
  * `attribute_name (str)`: The name of the attribute to remove.

##### `add_interface(interface)`

* Adds an interface to the device.
* Args:
  * `interface (str)`: The name of the interface to add.

##### `remove_interface(interface)`

* Removes an interface from the device.
* Args:
  * `interface (str)`: The name of the interface to remove.

##### `update_fqdn()`

* Updates the fully qualified domain name based on the hostname and site 
name.

##### `extract_hostname_site(fqdn)`

* Extracts the hostname and site name from a fully qualified domain name.
* Args:
  * `fqdn (str)`: The fully qualified domain name.
* Returns:
  * `tuple`: A tuple containing the hostname and site name.
* Raises:
  * `ValueError`: If the fully qualified domain name is invalid.

##### `get_active_interfaces()`

* Returns the list of active interfaces.
* Returns:
  * `list`: The list of active interfaces.

#### Interface Class

##### `__init__(name)`

* Initializes an Interface object.
* Args:
  * `name (str)`: The name of the interface.

##### `assign_ip_address(ip_address)`



* Assigns an IP address to the interface.
* Args:
  * `ip_address (str or ipaddress.IPv4Interface)`: The IP address to 
assign to the interface. It can be a string representing the IP address 
(e.g., '192.168.1.1') or an ipaddress.IPv4Interface object.
* Raises:
  * `ValueError`: If the provided IP address is invalid.

##### `remove_ip_address()`

* Removes the assigned IP address from the interface.

##### `__str__()`

* Returns a string representation of the interface.
* Returns:
  * `str`: The string representation of the interface.

##### `__repr__()`

* Returns a detailed string representation of the interface.
* Returns:
  * `str`: The detailed string representation of the interface.



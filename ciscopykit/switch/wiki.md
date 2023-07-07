# `switch.py`
---

This module provides a `Switch` class that represents a switch and offers methods for generating and configuring switch settings.

## Installation
No installation is required. Simply import the `Switch` class from the module.

```python
from switch import Switch
```

## Usage
### Creating a Switch
To create a switch object, use the following code:

```python
switch = Switch(model, host_name, ports, active_ports=None)
```

- `model`: Specifies the switch model.
- `host_name`: Specifies the hostname of the switch.
- `ports`: Specifies a list of all switch ports.
- `active_ports`: (Optional) Specifies a list of active switch ports. If not provided, all ports are considered active.

### Setting and Getting Switch Properties
You can set and get various properties of the switch using the following methods:

```python
switch.set_model(model)
model = switch.get_model()

switch.set_ports(ports)
ports = switch.get_ports()

switch.set_active_ports(active_ports)
active_ports = switch.get_active_ports()

switch.set_power_consumption(power_consumption)
power_consumption = switch.get_power_consumption()
```

### Generating Switch Configuration
To generate the switch configuration, use the `get_config()` method:

```python
config = switch.get_config(ip_dict, vlan_dict=None, vtp_domain=None, vtp_mode=None)
```

- `ip_dict`: A dictionary containing VLAN IP addresses. The keys are the VLANs, and the values are the corresponding IP addresses.
- `vlan_dict`: (Optional) A dictionary mapping VLAN names to VLAN IDs.
- `vtp_domain`: (Optional) The VTP domain name.
- `vtp_mode`: (Optional) The VTP mode.

The method returns the generated switch configuration as a string.

### Additional Methods
The `Switch` class provides the following additional methods:

- `generate_vlan_interface_config(vlan)`: Generates the configuration for a VLAN interface.
- `generate_physical_interface_config(interface)`: Generates the configuration for a physical interface.
- `generate_ip_address(name, prefix_length=24)`: Generates an IP address based on the provided name and prefix length.
- `get_next_ip_address(subnet)`: Returns the next available IP address in a subnet.
- `configure_vlan_interface(vlan, ip_dict=None)`: Generates the configuration for a VLAN interface with an IP address from the `ip_dict`.
- `configure_vtp(vtp_domain, vtp_mode=None)`: Generates the configuration for VTP (VLAN Trunking Protocol).

### Static Methods
The module also provides the following static methods that can be used independently:

- `convert_str_to_ipv4_interface(ip_mask)`: Converts a string representation of an IP address and subnet mask to an `IPv4Interface` object.
- `validate_ip_address(ip_address)`: Validates if an IP address is valid.

## Example
Here's an example demonstrating how to use the `Switch` class:

```python
from switch import Switch

switch = Switch("Cisco 3750", "LA_SW1", ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2", "VLAN10", "VLAN20"], ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2"])
ip_dict = {'VLAN10': '10.0.0.1/24', 'VLAN20': '20.0.0.1/24'}
vlan_dict = {'VLAN10': 'Sales', 'VLAN20': 'Marketing'}
vtp_domain = 'mydomain'

config = switch.get_config(ip_dict, vlan_dict, vtp_domain, vtp_mode='server')
print(config)
```

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
This module utilizes the `ipaddress` module to handle IP address manipulation and validation.


# `l3_switch.py`

The `L3Switch` class is a subclass of the `Switch` class, which represents a Layer 3 switch. It extends the functionality of the base `Switch` class by adding support for configuring routing protocols and generating switch configurations with VLAN and physical interface IP addresses.

## Installation
No installation is required. Simply import the `L3Switch` class from the `switch` module.

```python
from switch import L3Switch
```

## Usage
### Creating an L3 Switch
To create an L3 switch object, use the following code:

```python
l3_switch = L3Switch(model, ports, active_ports, routing_protocol, subnet)
```

- `model`: Specifies the switch model.
- `ports`: Specifies a list of all switch ports.
- `active_ports`: Specifies a list of active switch ports.
- `routing_protocol`: Specifies the routing protocol to configure on the switch (e.g., "OSPF", "EIGRP").
- `subnet`: Specifies the subnet for IP address generation.

### Setting and Getting L3 Switch Properties
You can set and get various properties of the L3 switch using the following methods inherited from the base `Switch` class:

```python
l3_switch.set_model(model)
model = l3_switch.get_model()

l3_switch.set_ports(ports)
ports = l3_switch.get_ports()

l3_switch.set_active_ports(active_ports)
active_ports = l3_switch.get_active_ports()

l3_switch.set_power_consumption(power_consumption)
power_consumption = l3_switch.get_power_consumption()
```

In addition, the `L3Switch` class provides the following methods:

```python
l3_switch.set_routing_protocol(routing_protocol)
routing_protocol = l3_switch.get_routing_protocol()

config = l3_switch.generate_config(ip_dict)
```

### Configuring Routing Protocol
To configure the routing protocol on the L3 switch, use the `configure_routing_protocol()` method:

```python
routing_protocol_config = l3_switch.configure_routing_protocol()
```

The method returns the configuration specific to the configured routing protocol.

### Generating L3 Switch Configuration
To generate the switch configuration, use the `generate_config()` method:

```python
config = l3_switch.generate_config(ip_dict)
```

- `ip_dict`: A dictionary containing the IP addresses for VLANs and physical interfaces. The keys are the interface names, and the values are the corresponding IP addresses with subnet masks.

The method returns the generated switch configuration as a string.

## Example
Here's an example demonstrating how to use the `L3Switch` class:

```python
from switch import L3Switch

l3_switch = L3Switch("Cisco 3750", ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2", "VLAN10", "VLAN20"], ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2"], "OSPF", "10.0.0.0/16")
ip_dict = {'VLAN10': '10.0.0.1/24', 'VLAN20': '20.0.0.1/24', 'GigabitEthernet1/0/1': '192.168.0.1/24'}
routing_protocol = l3_switch.get_routing_protocol()

config = l3_switch.generate_config(ip_dict)
print(config)

routing_protocol_config = l3_switch.configure_routing_protocol()
print(routing_protocol_config)
```

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
This module utilizes the `ipaddress` module to handle IP address manipulation and validation.

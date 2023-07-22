# `routing` package

## Modules

### `static_routing.py`

This module provides functions to configure static routes and route redistribution for Cisco devices.

## Functions:

### `configure_static_route(destination, next_hop, administrative_distance=1)`

Configures a static route on the device.

**Parameters:**
- destination (str): The destination network address in CIDR notation (e.g., '10.10.10.0/24').
- next_hop (str): The IP address of the next hop.
- administrative_distance (int, optional): The administrative distance for the static route. Default is 1.

**Returns:**
- str: Configuration command for the static route.

### `configure_default_route(next_hop)`
Configures a default static route on the Cisco IOS device.

**Parameters:**
- next_hop (str or ipaddress.IPv4Address): The next-hop IP address or exit interface for the default static route.

**Returns:**
- str: The configuration command for adding the default static route.

**Raises:**
- ValueError: If the next_hop is not a valid IPv4 address.

### `configure_route_redistribution(source_protocol, ospf_id=None, eigrp_as=None)`
Configures route redistribution between routing protocols.

**Parameters:**
- source_protocol (str): The source routing protocol from which routes will be redistributed. Supported values are: 'static', 'rip', 'eigrp', 'ospf'.
- ospf_id (int, optional): The OSPF process ID if the source_protocol is 'ospf'.
- eigrp_as (int, optional): The EIGRP AS number if the source_protocol is 'eigrp'.

**Returns:**
- str: The configuration commands for route redistribution.

**Raises:**
- ValueError: If source_protocol is not a supported routing protocol.
- ValueError: If ospf_id or eigrp_as is specified for an unsupported protocol.

## Example Usage:

```python
import static_routes

# Example 1: Configure a static route
destination = '192.168.1.0/24'
next_hop = '10.0.0.1'
administrative_distance = 5

static_route_config = static_routes.configure_static_route(destination, next_hop, administrative_distance)
print(static_route_config)

# Example 2: Configure a default route
default_next_hop = '192.168.0.1'

default_route_config = static_routes.configure_default_route(default_next_hop)
print(default_route_config)

# Example 3: Configure route redistribution
source_protocol = 'ospf'
ospf_id = 1

redistribution_config = static_routes.configure_route_redistribution(source_protocol, ospf_id=ospf_id)
print(redistribution_config)
```

This module provides a set of functions that allow you to configure static routes, default routes, and route redistribution for Cisco devices. You can use these functions to generate configuration commands specific to your network requirements. The example usage above demonstrates how to use each function and print the resulting configuration commands. Please make sure to replace the example parameters with your actual network information.

### `dynamic_routing.py`

This module provides classes to configure and generate dynamic routing protocols on Cisco devices.

#### Classes:

##### `DynamicRoutingProtocol`

Base class for dynamic routing protocols.

This class serves as a template for implementing dynamic routing protocols in CiscoPyKit. Subclasses must implement the `configure` and `generate_config` methods to configure the respective routing protocols on the device and generate the configuration.

**Attributes:**
- `networks` (list): A list of network addresses to be advertised.

**Methods:**
- `configure()`: Abstract method to configure the dynamic routing protocol on the device. Subclasses must implement this method.
- `generate_config()`: Abstract method to generate the configuration for the dynamic routing protocol. Subclasses must implement this method.

**Raises:**
- `NotImplementedError`: Raised when 'configure' and 'generate_config' methods are not implemented by the subclass.

##### `RIP`

Class representing the RIP (Routing Information Protocol) routing protocol.

RIP is a dynamic routing protocol that is widely used in small to medium-sized networks. It is a distance-vector protocol and uses hop count as the metric to calculate the best path to a destination network.

**Attributes:**
- `version` (int): The version of RIP to use (1 or 2).
- `networks` (list): A list of networks to advertise with RIP.
- `no_auto_summary` (bool, optional): Whether to disable auto-summary (default: False).
- `passive_interfaces` (list, optional): A list of interfaces to be set as passive (default: None).

**Methods:**
- `configure()`: Configures the RIP routing protocol on the device.
- `generate_config()`: Generates the configuration for the RIP routing protocol.

**Raises:**
- `ValueError`: If the version is not 1 or 2.

##### `OSPF`

Class representing the OSPF (Open Shortest Path First) routing protocol.

OSPF is a link-state routing protocol that is widely used in large networks. It uses Dijkstra's algorithm to calculate the shortest path to a destination network.

**Attributes:**
- `process_id` (int): The OSPF process ID.
- `router_id` (str): The OSPF router ID.
- `ospf_options` (dict, optional): Dictionary containing OSPF-specific options (default: None).

**Methods:**
- `configure()`: Configures OSPF routing protocol on the device.
- `generate_config()`: Generates the configuration for the OSPF routing protocol.

**Raises:**
- `ValueError`: If the process ID is not a positive integer.
- `ValueError`: If the provided IP addresses are not valid.

**Usage Example:**

```python
ospf_options = {
    'networks': ['192.168.1.0/24', '10.0.0.0/16'],
    'passive_interfaces': ['GigabitEthernet0/1', 'Serial0/0/0'],
    'default_route_interface': 'GigabitEthernet0/0'
}

ospf_instance = OSPF(process_id=10, router_id='6.6.6.6', ospf_options=ospf_options)

# Generate OSPF configuration
ospf_config = ospf_instance.generate_config()

# Print the generated configuration
print(ospf_config)
```

This module provides classes that allow you to configure and generate dynamic routing protocols such as OSPF and RIP on Cisco devices. The example usage above demonstrates how to use the `OSPF` class to configure OSPF with specific options and print the resulting configuration commands. 
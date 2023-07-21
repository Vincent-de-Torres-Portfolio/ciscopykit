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

``` python
# work in progress
```
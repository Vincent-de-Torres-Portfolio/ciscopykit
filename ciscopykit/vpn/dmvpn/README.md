# `dmvpn` Module

The DMVPN (Dynamic Multipoint Virtual Private Network) module in CiscoPyKit provides classes for configuring DMVPN hubs and spokes.
DMVPN is a flexible and scalable solution for building secure and dynamic VPN connections.

## Classes

### DMVPNHub

Class representing a DMVPN hub configuration.

**Attributes:**

- `tunnel_interface` (str): The name of the tunnel interface.
- `hub_ip` (str): The IP address of the DMVPN hub.
- `nhrp_group` (str): The NHRP group name.
- `nhrp_authentication` (str): The NHRP authentication string.

**Methods:**

- `configure()`: Generate the configuration for the DMVPN hub.

### DMVPNSpoke

Class representing a DMVPN spoke configuration.

**Attributes:**

- `tunnel_interface` (str): The name of the tunnel interface.
- `spoke_ip` (str): The IP address of the DMVPN spoke.
- `hub_ip` (str): The IP address of the DMVPN hub.
- `nhrp_group` (str): The NHRP group name.
- `nhrp_authentication` (str): The NHRP authentication string.

**Methods:**

- `configure()`: Generate the configuration for the DMVPN spoke.

## Usage

```python
from dmvpn import DMVPNHub, DMVPNSpoke

# Create a DMVPN hub configuration
hub = DMVPNHub(
    tunnel_interface="Tunnel0",
    hub_ip="10.0.0.1",
    nhrp_group="dmvpn_group",
    nhrp_authentication="cisco123"
)
hub_config = hub.configure()

print("DMVPN Hub Configuration:")
print(hub_config)

# Create a DMVPN spoke configuration
spoke = DMVPNSpoke(
    tunnel_interface="Tunnel1",
    spoke_ip="192.168.1.1",
    hub_ip="10.0.0.1",
    nhrp_group="dmvpn_group",
    nhrp_authentication="cisco123"
)
spoke_config = spoke.configure()

print("\nDMVPN Spoke Configuration:")
print(spoke_config)

```

For more information on the usage and attributes of the classes, refer to the module's docstrings.

## License

This module is licensed under the MIT License. See the LICENSE file for details.

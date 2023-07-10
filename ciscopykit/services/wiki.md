
# `services` 

---

## DHCP Service Module

The DHCP service module provides functions to configure DHCP on a network device. It allows you to set up a DHCP pool, network address, DNS address, default gateway, and excluded IP address range.

### Functions

- `config_dhcp(dhcp_pool_name, network_address, dns_address=None, dg=None, dns=None, exclude_ips=None)`: Configures DHCP on a network.

#### Parameters

- `dhcp_pool_name` (str): The name of the DHCP pool.
- `network_address` (str): The network address in CIDR format.
- `dns_address` (str, optional): The DNS address for the DHCP clients. If not provided, the default DNS address will be used.
- `dg` (str, optional): The default gateway address. If not provided, the first usable host address of the subnet will be used as the default gateway.
- `dns` (str, optional): Deprecated parameter, no longer used.
- `exclude_ips` (tuple(str, str), optional): The range of IP addresses to exclude from the DHCP pool. It should be specified as a tuple of two IP addresses representing the minimum and maximum addresses to exclude. If not provided, the first 100 usable host IP addresses and the subnet's first usable address will be excluded.

#### Usage Example

```python
from network_config.dhcp_service import config_dhcp

config = config_dhcp(dhcp_pool_name="V10", network_address="10.3.28.0/22", dns_address="10.3.20.100",
                     exclude_ips=("10.3.30.1", "10.3.30.100"))
print(config)
```

This will generate the DHCP configuration for the specified parameters.

## PAT Service Module

The PAT service module provides functions to configure Port Address Translation (PAT) on a network device. It allows you to set up the inside interface, network addresses, outside interface, and NAT pool.

### Functions

- `config_pat(nat_inside_interface, network_addresses, nat_outside_interface, nat_pool_start, nat_pool_end)`: Configures Port Address Translation (PAT) on a network device.

#### Parameters

- `nat_inside_interface` (str): The inside interface for NAT.
- `network_addresses` (list[str]): The list of network addresses to configure PAT for.
- `nat_outside_interface` (str): The outside interface for NAT.
- `nat_pool_start` (str): The start address of the NAT pool.
- `nat_pool_end` (str): The end address of the NAT pool.

#### Usage Example

```python
from network_config.pat_service import config_pat

config = config_pat(nat_inside_interface="eth0", network_addresses=["192.168.0.0/24", "10.0.0.0/16"],
                    nat_outside_interface="eth1", nat_pool_start="192.0.2.1", nat_pool_end="192.0.2.100")
print(config)
```

This will generate the PAT configuration for the specified parameters.


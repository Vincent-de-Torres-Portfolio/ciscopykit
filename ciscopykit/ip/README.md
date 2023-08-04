# CiscoPyKit - IP Module

## Overview

The `ip.py` module in CiscoPyKit provides functions for managing IP addresses, including performing VLSM (Variable Length Subnet Masking) and subnetting on IPv4 networks.

## Functions

### VLSM (Variable Length Subnet Masking)

The `vlsm` function allows you to perform VLSM on an IPv4 network. VLSM is a technique used to allocate IP addresses efficiently by dividing a network into smaller subnets of different sizes.

#### Parameters

- `network` (str): The IPv4 network in the format "x.x.x.x/y".
- `new_prefixes` (list): The list of new prefix lengths for each subnet in the network.

#### Returns

- `list`: The list of subnets created by the VLSM process.

#### Usage Example

```python
from ip import vlsm

network = "192.168.0.0/24"
new_prefixes = [26, 28, 29]
subnets = vlsm(network, new_prefixes)
print(subnets)
```

##### Output:

```
[IPv4Network('192.168.0.0/29'), IPv4Network('192.168.0.8/29'), IPv4Network('192.168.0.16/29'),
IPv4Network('192.168.0.24/29'), IPv4Network('192.168.0.32/29'), IPv4Network('192.168.0.40/29'),
IPv4Network('192.168.0.48/29'), IPv4Network('192.168.0.56/29')]
```

## Requirements

- Python 3.11
- ipaddress module

## License

This module is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

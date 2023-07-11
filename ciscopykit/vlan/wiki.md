
# VLAN Subpackage Wiki

The VLAN subpackage provides functionality for managing VLANs and VTP (VLAN Trunking Protocol) settings.

## VLANConfig Class

The `VLANConfig` class provides methods to create VLANs and configure VTP settings.

### Methods

#### `create_vlan(vlan_id, vlan_name)`

Creates a VLAN with the specified VLAN ID and VLAN name.

- `vlan_id` (int): VLAN ID.
- `vlan_name` (str): VLAN name.

Returns a tuple containing the VLAN configuration and interface configuration.

##### Usage Example:

```python
from vlan.config import VLANConfig

vlan_id = 10
vlan_name = "mgt"
config, interface_config = VLANConfig.create_vlan(vlan_id, vlan_name)

print(config)
print(interface_config)
```

Output:
```
vlan 10
name mgt

interface vlan 10
no shutdown
exit
```

#### `configure_vtp_domain(vtp_domain)`

Configures the VTP domain with the specified domain name.

- `vtp_domain` (str): VTP domain name.

Returns the VTP domain configuration.

##### Usage Example:

```python
from vlan.config import VLANConfig

vtp_domain = "example-domain"
config = VLANConfig.configure_vtp_domain(vtp_domain)

print(config)
```

Output:
```
vtp domain example-domain
```

#### `configure_vtp_mode(vtp_mode)`

Configures the VTP mode with the specified mode.

- `vtp_mode` (str): VTP mode.

Returns the VTP mode configuration.

##### Usage Example:

```python
from vlan.config import VLANConfig

vtp_mode = "server"
config = VLANConfig.configure_vtp_mode(vtp_mode)

print(config)
```

Output:
```
vtp mode server
```

## Usage

Here are some examples of how to use the VLAN subpackage for common tasks:

### Creating VLANs

To create a VLAN, use the `create_vlan` method of the `VLANConfig` class.

Example:

```python
from vlan.config import VLANConfig

vlan_id = 10
vlan_name = "mgt"
config, interface_config = VLANConfig.create_vlan(vlan_id, vlan_name)

print(config)
print(interface_config)
```

### Configuring VTP Domain

To configure the VTP domain, use the `configure_vtp_domain` method of the `VLANConfig` class.

Example:

```python
from vlan.config import VLANConfig

vtp_domain = "example-domain"
config = VLANConfig.configure_vtp_domain(vtp_domain)

print(config)
```

### Configuring VTP Mode

To configure the VTP mode, use the `configure_vtp_mode` method of the `VLANConfig` class.

Example:

```python
from vlan.config import VLANConfig

vtp_mode = "server"
config = VLANConfig.configure_vtp_mode(vtp_mode)

print(config)
```

## Contributing

Contributions to the VLAN subpackage are welcome! If you have any ideas for improvement, find any issues, or want to add new features, please follow the contribution guidelines mentioned in the [Contributing](/README.md#contributing) section of the README.

## License

This VLAN subpackage is open-source and is distributed under the [MIT License](/LICENSE.md). 

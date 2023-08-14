# EtherChannel Subpackage

A subpackage in the CiscoPyKit collection for configuring Layer 2 and Layer 3 EtherChannels.

## Installation

To use the `etherchannel` subpackage, you need to have the `ciscopykit` package installed. You can install it using pip:

```bash
pip install ciscopykit
```

## Usage

### Layer 2 EtherChannel

To configure a Layer 2 EtherChannel, you can use the CLI command as follows:

```bash
ciscopykit layer2 <port_channel_number> <interfaces> [--allowed_vlans <vlan_list>]
```

Example:

```bash
ciscopykit layer2 1 "GigabitEthernet0/1,GigabitEthernet0/2" --allowed_vlans "10,20"
```

### Layer 3 EtherChannel

To configure a Layer 3 EtherChannel, you can use the CLI command as follows:

```bash
ciscopykit layer3 <port_channel_number> <interfaces> <ip_address> <subnet_mask>
```

Example:

```bash
ciscopykit layer3 2 "GigabitEthernet0/3,GigabitEthernet0/4" 192.168.1.1 255.255.255.0
```

Replace `<port_channel_number>`, `<interfaces>`, `<vlan_list>`, `<ip_address>`, and `<subnet_mask>` with the actual values for your configuration.

## License

This subpackage is distributed under the MIT License. See [LICENSE](LICENSE) for more information.
```

<!-- ![logo](assets/img/logo.svg) -->
# **`ciscopykit`**

---
 
![logo](assets/img/logo.svg)

---

CiscoPyKit is a network management toolkit for Cisco devices. It provides classes and methods to manage network devices, interfaces, and configurations.

## Features

---

- Device management: Add, remove, and modify Cisco devices.
- Interface management: Assign and remove IP addresses for network interfaces.
- Configuration management: Retrieve and update device configurations.
- Network visualization: Generate network topology diagrams.
- DHCP service configuration: Configure DHCP on a network device.
- PAT service configuration: Configure Port Address Translation (PAT) on a network device.
- L3 switch configuration: Generate and configure L3 switch settings.

## Installation

---

Use pip to install CiscoPyKit:

```bash
pip install ciscopykit
```

## Usage

---

The package provides a command-line interface (CLI) that uses argparse to configure network services. Here's how you can use each subpackage on the command line:

### Device Management

To manage Cisco devices, use the following command:

```
python -m ciscopykit.device.app <command> [<args>]
```

Available commands:

- `add`: Add a new device.
- `remove`: Remove an existing device.
- `modify`: Modify an existing device.
- `list`: List all devices.

Example usage:

```
# Add a new device
python -m ciscopykit.device.app add --hostname R1 --ip 192.168.1.1 --username admin --password secret

# Modify an existing device
python -m ciscopykit.device.app modify --hostname R1 --ip 192.168.1.1 --username admin --password new_secret

# Remove an existing device
python -m ciscopykit.device.app remove --hostname R1

# List all devices
python -m ciscopykit.device.app list
```

### Interface Management

To manage interfaces on Cisco devices, use the following command:

```
python -m ciscopykit.interface.app <command> [<args>]
```

Available commands:

- `assign`: Assign an IP address to an interface.
- `remove`: Remove an IP address from an interface.
- `list`: List all interfaces.

Example usage:

```
# Assign an IP address to an interface
python -m ciscopykit.interface.app assign --device R1 --interface GigabitEthernet0/0 --ip 192.168.1.1/24

# Remove an IP address from an interface
python -m ciscopykit.interface.app remove --device R1 --interface GigabitEthernet0/0

# List all interfaces
python -m ciscopykit.interface.app list --device R1
```

### Configuration Management

To manage configurations on Cisco devices, use the following command:

```
python -m ciscopykit.config.app <command> [<args>]
```

Available commands:

- `get`: Retrieve the configuration of a device.
- `update`: Update the configuration of a device.

Example usage:

```
# Retrieve the configuration of a device
python -m ciscopykit.config.app get --device R1

# Update the configuration of a device
python -m ciscopykit.config.app update --device R1 --config-file config.txt
```

### DHCP Service Configuration

To configure DHCP on a network device, use the following command:

```
python -m ciscopykit.services.app dhcp <dhcp_pool_name> <network_address> [--dns_address <dns_address>] [--dg <default_gateway>] [--exclude_ips <min> <max>]
```

Example usage:

```
python -m ciscopykit.services.app dhcp V10 "10.3.28.0/22" --dns_address "10.3.20.100" --exclude_ips "10.3.30.1" "10.3.30.100"
```

### PAT Service Configuration

To configure Port Address Translation (PAT) on a network device, use the following command:

```
python -m ciscopykit.services.app pat <nat_inside_interface> <network_address1> <network_address2> ... <nat_outside_interface> <nat_pool_start> <nat_pool_end>
```

Example usage:

```
python -m ciscopykit.services.app pat eth0 "192.168.0.0/24" "10.0.0.0/16" eth1 "192.0.2.1" "192.0.2.100"
```

### L3 Switch Configuration

To generate and configure L3 switch settings, use the following command:

```
python -m ciscopykit.switch.app <switch_model> <port_list> <active_port_list> <routing_protocol> [--ip-dict <ip_dictionary>] [--hostname <switch_hostname>] [--subnet <subnet>] [--save-config <config_file_path>]
```

Example usage:

```
python -m ciscopykit.switch.app "Cisco 3750" "GigabitEthernet1/0/1,GigabitEthernet1/0/2,VLAN10,VLAN20" "GigabitEthernet1/0/1,GigabitEthernet1/0/2" "OSPF" --ip-dict "{'VLAN10': '10.0.0.1/24', 'VLAN20': '20.0.0.1/24', 'Gi0/0':'10.10.11.1/30'}" --hostname "LA_SW1" --subnet "10.0.0.0/16" --save-config ./config.txt
```

For more detailed usage instructions, please refer to the [documentation](https://github.com/devinci-it/ciscopykit).

## Contributing

Contributions are welcome! If you have any bug reports, feature requests, or suggestions, please open an issue on GitHub. If you would like to contribute code, please fork the repository, make your changes, and submit a pull request.

## License

CiscoPyKit is licensed under the [MIT License](LICENSE).
```

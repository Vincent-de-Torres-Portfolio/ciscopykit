## `switch`

This script allows you to configure a switch using command-line arguments.

### Usage

```
python switch.py [options]
```

### Options

- `--model MODEL`: Specifies the switch model. This should be a string representing the model name of the switch.
- `--hostname HOSTNAME`: Specifies the switch hostname. This should be a string representing the hostname of the switch.
- `--ports PORT [PORT ...]`: Specifies the switch ports. This should be one or more strings representing the ports of the switch.
- `--active-ports PORT [PORT ...]`: Specifies the active ports. This should be one or more strings representing the active ports of the switch.
- `--ip-dict INTERFACE:IP_ADDRESS[,INTERFACE:IP_ADDRESS ...]`: Specifies the mapping of interfaces to IP addresses. This should be a comma-separated string in the format `INTERFACE:IP_ADDRESS`, where `INTERFACE` is the port/interface name and `IP_ADDRESS` is the corresponding IP address.

### Method Explanation

- `Switch(model, host_name, ports, active_ports=None)`: Initializes a `Switch` object with the specified model, hostname, ports, and active ports. The `active_ports` parameter is optional and defaults to an empty list if not provided.
- `Switch.set_active_ports(active_ports)`: Sets the active ports of the switch to the provided list of active ports.
- `Switch.get_config(ip_dict)`: Generates the configuration for the switch based on the provided IP dictionary. The `ip_dict` parameter is a dictionary that maps interfaces to IP addresses.
- `Switch.generate_init_config(hostname, site, interface_range="GigabitEthernet0/0/0-24", static_pass="cisco", motd="Welcome to the Cisco network!")`: Generates the initial configuration for the switch based on the provided hostname, site, interface range, static password, and MOTD (Message of the Day).
- `Switch.generate_vlan_config(vlan)`: Generates the configuration for a VLAN with the specified VLAN ID.
- `Switch.generate_physical_interface_config(interface, ip_dict)`: Generates the configuration for a physical interface with the specified interface name and IP dictionary.
- `Switch.convert_str_to_ipv4_interface(ip_mask)`: Converts a string representation of an IP address and subnet mask into an `IPv4Interface` object.
- `Switch.validate_ip_address(ip_address)`: Validates if the provided string is a valid IP address.

### Example

```
python switch.py --model Cisco3650 --hostname Switch1 --ports GigabitEthernet0/1 GigabitEthernet0/2 --active-ports GigabitEthernet0/1 --ip-dict "GigabitEthernet0/1:192.168.1.1/24,GigabitEthernet0/2:192.168.2.1/24"
```

This example configures a switch with the following settings:
- Model: Cisco 3650
- Hostname: Switch1
- Ports: GigabitEthernet0/1, GigabitEthernet0/2
- Active Ports: GigabitEthernet0/1
- IP Dictionary: GigabitEthernet0/1 -> 192.168.1.1/24, GigabitEthernet0/2 -> 192.168.2.1/24

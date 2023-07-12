# CiscoPyKit - Network Management Toolkit for Cisco Devices

![logo](assets/img/logo.svg)

CiscoPyKit is a powerful and comprehensive network management toolkit designed specifically for Cisco devices. It simplifies the management and configuration of network devices, interfaces, and services, while also providing advanced features for network security.

## Features

- Device Management: Add, remove, and modify Cisco devices effortlessly.
- Interface Management: Assign and remove IP addresses for network interfaces with ease.
- Configuration Management: Retrieve and update device configurations seamlessly.
- Network Visualization: Generate clear and intuitive network topology diagrams for better visualization.
- DHCP Service Configuration: Configure DHCP on network devices to efficiently manage IP address assignment.
- Port Address Translation (PAT) Configuration: Configure Port Address Translation (PAT) for simplified network address translation.
- L3 Switch Configuration: Generate and configure Layer 3 switch settings effortlessly.
- LAN Security Features:
  - Switchport Security: Configure security settings for switchports to prevent unauthorized access.
  - VLAN Security: Manage VLANs and configure VLAN-based security policies to control traffic flow.
  - DHCP Snooping: Enable and configure DHCP snooping to protect against rogue DHCP servers.
  - Dynamic ARP Inspection: Validate ARP packets to prevent ARP spoofing attacks.
  - STP Security: Enhance Spanning Tree Protocol (STP) security to safeguard against STP-based attacks.

For detailed instructions and further information, please refer to the [README.md](#features) on each package.

## Installation

Use pip to install CiscoPyKit:

```bash
pip install ciscopykit
```

## Usage

CiscoPyKit provides a user-friendly command-line interface (CLI) that simplifies the configuration and management of Cisco devices. Below are examples of how to use different subpackages:

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

To generate and configure Layer 3 switch settings, use the following command:

```
python -m ciscopykit.switch.app <switch_model> <port_list> <active_port_list> <routing_protocol> [--ip-dict <ip_dictionary>] [--hostname <switch_hostname>] [--subnet <subnet>] [--save-config <config_file_path>]
```

Example usage:

```
python -m ciscopykit.switch.app "Cisco 3750" "GigabitEthernet1/0/1,GigabitEthernet1/0/2,VLAN10,VLAN20" "GigabitEthernet1/0/1,GigabitEthernet1/0/2" "OSPF" --ip-dict "{'VLAN10': '10.0.0.1/24', 'VLAN20': '20.0.0.1/24', 'Gi0/0':'10.10.11.1/30'}" --hostname "LA_SW1" --subnet "10.0.0.0/16" --save-config ./config.txt
```



## LAN Security Features

CiscoPyKit also provides advanced LAN Security features to enhance network security and protect against various threats. These features include:

### Switchport Security Module

The Switchport Security module enables you to configure security settings for switchports, preventing unauthorized access to the network. It offers fine-grained control over switchport security parameters such as the maximum number of MAC addresses allowed, violation actions, aging time, and sticky MAC address configuration. 

To use the Switchport Security module, import the `configure_switchport_security` function from `lan_security.switchport_security` and follow the provided usage examples to configure switchport security settings tailored to your network requirements.

### Usage

```
# Assuming proper module imports

interface = "GigabitEthernet1/0/1"
max_mac = 5
config = configure_switchport_security(interface, max_mac)
print(config)
```

Output:
```
interface GigabitEthernet1/0/1
switchport mode access
switchport port-security
switchport port-security maximum 5
switchport port-security violation restrict
switchport port-security mac-address sticky
```

### VLAN Security (Coming Soon)

The VLAN Security module provides the capability to manage VLANs and configure VLAN-based security policies. It allows you to create, delete, and modify VLANs, as well as define security policies that control traffic flow between VLANs, enhancing network segmentation and security.

### DHCP Snooping (Coming Soon)

The

 DHCP Snooping module enables you to enable and configure DHCP snooping on network devices. By actively monitoring DHCP traffic and verifying DHCP server legitimacy, DHCP snooping prevents rogue DHCP servers from distributing malicious IP addresses and enhances overall network security.

### Dynamic ARP Inspection (Coming Soon)

The Dynamic ARP Inspection module validates ARP packets to prevent ARP spoofing attacks, which can lead to unauthorized network access and data breaches. By inspecting ARP traffic and filtering out malicious or unauthorized ARP packets, Dynamic ARP Inspection enhances network security and prevents potential threats.

### STP Security (Coming Soon)

The STP Security module enhances Spanning Tree Protocol (STP) security to protect against STP-based attacks, such as BPDU spoofing or manipulation. By applying appropriate STP security measures, such as BPDU guard or root guard, you can ensure the integrity and stability of your network infrastructure.

Stay tuned for the upcoming releases of these LAN Security features!

## Contributing

Contributions to CiscoPyKit are welcome! If you encounter any issues, have feature requests, or want to contribute code, please feel free to open an issue or submit a pull request on GitHub.

## License

CiscoPyKit is licensed under the [MIT License](LICENSE).
# CiscoPyKit - Network Management Toolkit for Cisco Devices

![logo](assets/img/logo.svg)

CiscoPyKit is a powerful and comprehensive network management toolkit designed specifically for Cisco devices. It simplifies the management and configuration of network devices, interfaces, and services, while also providing advanced features for network security.

## Features

- Device Management: Add, remove, and modify Cisco devices effortlessly. *
- Interface Management: Assign and remove IP addresses for network interfaces with ease. *
- Configuration Management: Retrieve and update device configurations seamlessly. *
-  IP Services Features :
    - DHCP Service Configuration: Configure DHCP on network devices to efficiently manage IP address assignment.
    - Port Address Translation (PAT) Configuration: Configure Port Address Translation (PAT) for simplified network address translation.
    - L3 Switch Configuration: Generate and configure Layer 3 switch settings effortlessly.
- LAN Security Features:
  - [Switchport Security](lan_security/README.md#switchport-security-module): Configure security settings for switchports to prevent unauthorized access.
  - [VLAN Security](lan_security/README.md#vlan-security-module): Manage VLANs and configure VLAN-based security policies to control traffic flow.
  - [DHCP Snooping](lan_security/README.md#dhcp-snooping-module): Enable and configure DHCP snooping to protect against rogue DHCP servers.
  - [Dynamic ARP Inspection](lan_security/README.md#dynamic-arp-inspection-module): Validate ARP packets to prevent ARP spoofing attacks.
  - [STP Security](lan_security/README.md#stp-security-module): Enhance Spanning Tree Protocol (STP) security to safeguard against STP-based attacks.
  
For detailed information on each feature, please refer to the README.md files in the corresponding subpackages.

## Package Updates

```
ciscopykit
├── ...
├── lan_security (NEW)
│   ├── switchport_security.py
│   ├── vlan_security.py
│   ├── dhcp_snooping.py
│   ├── dynamic_arp_inspection.py
│   ├── stp_security.py
│   └── README.md
│   
├── routing (WIP)
│   ├── static_routes.py 
│   ├── dynamic_routing.py
│   └── README.md
│   
└── README.md

```

The package is organized into various subpackages, each focused on a specific aspect of network management. Within each subpackage, you will find modules and functions tailored to handle specific tasks related to the subpackage's theme.

- The `device` module deals with device management, allowing you to add, remove, modify, and list Cisco devices.
- The `interface` module handles interface management, enabling you to assign and remove IP addresses for network interfaces.
- The `services` subpackage contains modules for configuring DHCP and PAT services on network devices.
- The `switch` subpackage provides functions to generate and configure switch settings.
- The `vlan` subpackage provides functions to generate and configure vlan and vtp settings.
- The `lan_security` subpackage includes modules for LAN security features like switchport security, VLAN security, DHCP snooping, dynamic ARP inspection, and STP security.
- The `routing` subpackage (Coming Soon) will contain modules for configuring static and dynamic routing protocols.

For detailed information on the functions and features within each subpackage, please refer to the corresponding README.md file.

## Installation

Use pip to install CiscoPyKit:

```bash
pip install ciscopykit
```

## Usage

CiscoPyKit provides a user-friendly command-line interface (CLI) that simplifies the configuration and management of Cisco devices. For detailed information on the functions and features within each subpackage, please refer to the corresponding README.md file.

## Contributing

Contributions to CiscoPyKit are welcome! If you encounter any issues, have feature requests, or want to contribute code, please feel free to open an issue or submit a pull request on GitHub.

## License

CiscoPyKit is licensed under the [MIT License](LICENSE).

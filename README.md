![logo](assets/img/logo.svg)


# ciscopykit

ciscopykit is a Python package designed to automate the generation of Cisco IOS commands and provide an easy way to track device configurations. It offers functionalities organized into various subpackages, each focusing on a specific aspect of network management. This README aims to provide an overview of the package structure and its functionalities.

## Features

- **Device Management**: The `device` module facilitates device management tasks such as adding, removing, modifying, and listing Cisco devices.
- **Interface Configuration**: The `interface` module handles interface management, allowing users to assign and remove IP addresses for network interfaces.
- **Services Configuration**: The `services` subpackage contains modules for configuring DHCP and PAT services on network devices.
- **Switch Settings**: The `switch` subpackage provides functions to generate and configure switch settings.
- **VLAN Configuration**: The `vlan` subpackage offers functionalities to generate and configure VLAN and VTP settings.
- **LAN Security**: The `lan_security` subpackage includes modules for LAN security features, covering switchport security, VLAN security, DHCP snooping, dynamic ARP inspection, and STP security.
- **Routing Configuration**: The `routing` subpackage contains modules for configuring static and dynamic routing protocols.

## Directory Structure

```
ciscopykit/
├── app.py
├── device.py
├── entry_point.py
├── etherchannel
│   ├── cli.py
│   ├── etherchannel.py
│   ├── __init__.py
│   └── README.md
├── help
│   ├── demo.py
│   ├── device.md
│   └── help.md
├── __init__.py
├── interface.py
├── ip
│   ├── __init__.py
│   ├── README.md
│   └── vlsm.py
├── README.md
├── routing
│   ├── app.py
│   ├── dynamic_routing.py
│   ├── __init__.py
│   ├── README.md
│   └── static_routing.py
├── security
│   ├── acl
│   │   ├── acl.py
│   │   ├── __init__.py
│   │   └── README.md
│   ├── __init__.py
│   └── lan_security
│       ├── app.py
│       ├── dhcp_snooping.py
│       ├── dynamic_arp_inspection.py
│       ├── __init__.py
│       ├── README.md
│       ├── stp_security.py
│       ├── switchport_security.py
│       ├── vlan_security.py
│       └── wiki.md
├── services
│   ├── app.py
│   ├── dhcp_service.py
│   ├── help.md
│   ├── __init__.py
│   ├── pat_service.py
│   └── wiki.md
├── switch
│   ├── app.py
│   ├── help.md
│   ├── __init__.py
│   ├── l2_switch.py
│   ├── l3_switch.py
│   ├── switch.py
│   └── wiki.md
├── templates
│   ├── generate_router_config.py
│   ├── logo.svg
│   ├── placeholder.txt
│   └── README.md
├── vlan
│   ├── app.py
│   ├── __init__.py
│   ├── README.md
│   ├── vlan.py
│   └── wiki.md
└── vpn
    ├── dmvpn
    │   ├── dmvpn.py
    │   ├── __init__.py
    │   └── README.md
    ├── gre
    │   ├── gre.py
    │   ├── __init__.py
    │   └── README.md
    └── README.md

```

## Getting Started

To install ciscopykit, you can use pip:

```bash
pip install ciscopykit
```

## Contribution

Contributions to ciscopykit are welcome! If you have any ideas, enhancements, or bug fixes, feel free to open an issue or submit a pull request on [GitHub](https://github.com/devinci-it/ciscopykit).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

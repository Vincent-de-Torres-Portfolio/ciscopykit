

<!-- ![logo](assets/img/logo.svg) -->
# **`ciscopykit`**
![logo](assets/banner.png)


---

CiscoPyKit is a network management toolkit for Cisco devices. It provides classes and methods to manage network devices, interfaces, and configurations.

## Features

- Device management: Add, remove, and modify Cisco devices.
- Interface management: Assign and remove IP addresses for network interfaces.
- Configuration management: Retrieve and update device configurations.
- Network visualization: Generate network topology diagrams.

## Installation

Use pip to install CiscoPyKit:

```bash
pip install ciscopykit
```

## Usage

```python
from ciscopykit import Device, Interface

# Create a device object
device = Device(device_type='Router', hostname='R1', site='SiteA')

# Create an interface object and assign an IP address
interface = Interface(name='GigabitEthernet0/0')
interface.assign_ip_address('192.168.1.1/24')

# Add the interface to the device
device.add_interface(interface)

# Print the device information
print(device)
print(device.get_active_interfaces())

# Modify the device hostname
device.modify_hostname('R1-new')

# Remove the assigned IP address from the interface
interface.remove_ip_address()
```

## Help Documentation

Additional documentation and usage examples can be found in the `/ciscopykit/help` directory. Please refer to the following files for more information:

- [Device Documentation](ciscopykit/help/device.md): Explains the methods and usage of the Device class.
- [Help Documentation](ciscopykit/help/help.md): Provides general help and guidelines for using CiscoPyKit.

For more detailed usage instructions, please refer to the [documentation](https://github.com/devinci-it/ciscopykit).

## Contributing

Contributions are welcome! If you have any bug reports, feature requests, or suggestions, please open an issue on GitHub. If you would like to contribute code, please fork the repository, make your changes, and submit a pull request.

## License

CiscoPyKit is licensed under the [MIT License](LICENSE).

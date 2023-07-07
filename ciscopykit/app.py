"""
app.py

This module contains the main application logic for managing network 
devices and interfaces.
"""

from ciscopykit.device import Device
from ciscopykit.interface import Interface


def main():
    # Create a device
    device = Device(hostname="router1", site="HQ")

    # Create an interface
    interface = Interface(name="eth0", ip_address="192.168.1.1")

    # Add the interface to the device
    device.add_interface(interface)

    # Print the device information
    print(device)

    # Print the active interfaces
    active_interfaces = device.get_active_interfaces()
    for interface in active_interfaces:
        print(interface)


if __name__ == "__main__":
    main()

#  python app.py --model "Cisco 3750" --ports "GigabitEthernet1/0/1,GigabitEthernet1/0/2,VLAN10,VLAN20" --active-ports "GigabitEthernet1/0/1,GigabitEthernet1/0/2" --routing-protocol "OSPF" --ip-dict "{'VLAN10': '10.0.0.1/24', 'VLAN20': '20.0.0.1/24', 'Gi0/0':'10.10.11.1/30'}" --hostname "LA_SW1" --subnet "10.0.0.0/16"
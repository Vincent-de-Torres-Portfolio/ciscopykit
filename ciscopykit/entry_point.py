from ciscopykit.device import Device
from ciscopykit.interface import Interface


def main():
    # Create a sample network configuration

    # Create devices
    router = Device(device_type="Router", hostname="router1", site="core")
    l3_switch = Device(device_type="L3 Switch", hostname="l3switch1", 
site="core")
    l2_switch = Device(device_type="L2 Switch", hostname="l2switch1", 
site="access")
    endpoint = Device(device_type="Endpoint", hostname="endpoint1", 
site="access")

    # Create interfaces
    router_interface = Interface(name="GigabitEthernet0/1")
    l3_switch_interface = Interface(name="GigabitEthernet0/1")
    l2_switch_interface = Interface(name="FastEthernet0/1")
    endpoint_interface = Interface(name="Ethernet0/1")

    # Assign IP addresses to interfaces
    router_interface.assign_ip_address("192.168.1.1/24")
    l3_switch_interface.assign_ip_address("192.168.1.2/24")
    l2_switch_interface.assign_ip_address("192.168.1.3/24")
    endpoint_interface.assign_ip_address("192.168.1.4/24")

    # Add interfaces to devices
    router.add_interface(router_interface)
    l3_switch.add_interface(l3_switch_interface)
    l2_switch.add_interface(l2_switch_interface)
    endpoint.add_interface(endpoint_interface)

    # Print the network configuration
    print("Network Configuration:")
    print(router)
    print(l3_switch)
    print(l2_switch)
    print(endpoint)

    # Modify device attributes
    router.modify_hostname("router2")
    l3_switch.modify_site("distribution")
    endpoint.remove_attribute("site")

    # Print the updated network configuration
    print("\nUpdated Network Configuration:")
    print(router)
    print(l3_switch)
    print(l2_switch)
    print(endpoint)


if __name__ == "__main__":
    main()


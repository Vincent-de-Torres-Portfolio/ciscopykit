import ipaddress
from ciscopykit.device import Device, Router
from ciscopykit.interface import Interface

def generate_router_config(hostname, ip_network, interfaces):
    # Create a router device
    router = Router(hostname, "SiteA", "Core")

    # Modify the hostname of the router
    router.modify_hostname(hostname)

    # Extract the site name from the provided IP network
    site = ip_network.split('.')[2]

    # Modify the site name of the router
    router.modify_site(site)

    # Generate the initial configuration for the router
    config = router.generate_init_config(hostname, site)

    # Create and configure interfaces
    for interface_data in interfaces:
        interface_name = interface_data['name']
        interface_ip = interface_data['ip']
        interface_subnet = str(interface_ip.network.netmask)

        # Create an interface object
        interface = Interface(interface_name)
        
        # Assign IP address to the interface
        interface.assign_ip_address(interface_ip)

        # Add the interface to the router
        router.add_interface(interface)

        # Generate the interface configuration for the interface
        interface_config = router.generate_interface_config(interface_name, str(interface_ip.ip), interface_subnet)

        # Append the interface configuration to the overall configuration
        config += interface_config

    # Write the configuration to a file
    with open("router-config.txt", "w") as file:
        file.write(config)

    print("Configuration file generated successfully.")

# Input parameters
hostname = "LA-R1"
ip_network = "192.168.1.0/24"
interfaces = [
    {'name': 'g0/0', 'ip': ipaddress.IPv4Interface('192.168.1.1/24')},
    {'name': 'g0/1', 'ip': ipaddress.IPv4Interface('192.168.3.2/24')},
    {'name': 'se0/0/0', 'ip': ipaddress.IPv4Interface('192.168.2.3/24')}
]

# Generate the router configuration
generate_router_config(hostname, ip_network, interfaces)

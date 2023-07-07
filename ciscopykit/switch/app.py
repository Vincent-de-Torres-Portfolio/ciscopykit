import ipaddress
class Switch:
    def __init__(self, model, host_name, ports, active_ports=None):
        self.model = model
        self.ports = ports
        self.host_name = host_name
        if active_ports is None:
            self.active_ports = []
        else:
            self.active_ports = active_ports

    def get_active_ports(self):
        return self.active_ports

    def set_active_ports(self, active_ports):
        self.active_ports = active_ports

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_ports(self):
        return self.ports

    def set_ports(self, ports):
        self.ports = ports

    def get_power_consumption(self):
        return self.power_consumption

    def set_power_consumption(self, power_consumption):
        self.power_consumption = power_consumption

    @staticmethod
    def generate_init_config(hostname, site, interface_range="GigabitEthernet0/0/0-24", static_pass="cisco", motd="Welcome to the Cisco network!"):
        # Generate configuration
        config = f'''
       !{'=' * 40}!
       ! {hostname}{' ' * (39 - len(hostname))}!      
       !{'=' * 40}!  

       enable
       configure terminal
       no ip domain-lookup
       hostname {hostname}
       username admin secret {static_pass}

       line console 0
       logging synchronous
       exit
       conf t
       ip domain-name {site}.ccna.com
       crypto key generate rsa
       1024

       banner motd ${motd}$
       enable secret {static_pass}
       line console 0
       password {static_pass}
       login
       exit

       line vty 0 4
       login local
       transport input ssh
       ip ssh version 2

       service password-encryption
                   '''
        return config

    def get_config(self, ip_dict):
        config = self.generate_init_config(hostname=self.host_name, site=self.host_name[:2])

        # Add interface configurations
        for port in self.active_ports:
            if port.startswith("VLAN"):
                config += self.generate_vlan_config(port)
            else:
                config += self.generate_physical_interface_config(port, ip_dict)

        return config

    @staticmethod
    def generate_vlan_config(vlan):
        return f'''
        vlan {vlan}
        name VLAN {vlan}
        exit
        '''


    def generate_physical_interface_config(self, interface, ip_dict):

        config = f'''
        interface {interface}
        '''

        ip_address = ip_dict[interface]
        interface = self.convert_str_to_ipv4_interface(ip_address)
        config += f"ip address {interface.ip} {interface.netmask}\n"

        config += "\t\tno shutdown\n"
        config += "\t\texit\n"
        return config

    @staticmethod
    def convert_str_to_ipv4_interface (ip_mask):
        return ipaddress.IPv4Interface(ip_mask)
    @staticmethod
    def validate_ip_address(ip_address):
        try:
            ipaddress.IPv4Interface(ip_address)
            return True
        except ValueError:
            return False


class L2Switch(Switch):
    def __init__(self, model, ports, power_consumption, vlan_support):
        super().__init__(model, ports, power_consumption)
        self.vlan_support = vlan_support

    def get_vlan_support(self):
        return self.vlan_support

    def set_vlan_support(self, vlan_support):
        self.vlan_support = vlan_support


class L3Switch(Switch):
    def __init__(self, model, ports, routing_protocol):
        super().__init__(model, ports)
        self.routing_protocol = routing_protocol

    def get_routing_protocol(self):
        return self.routing_protocol

    def set_routing_protocol(self, routing_protocol):
        self.routing_protocol = routing_protocol

#
# #DEMO
# # Create a Switch object
# switch = Switch(model="Cisco", host_name="Switch1", ports=["GigabitEthernet0/1", "GigabitEthernet0/2"])
#
# # Set the active ports
# active_ports = ["GigabitEthernet0/1", "GigabitEthernet0/2"]
# switch.set_active_ports(active_ports)
#
# # Dictionary of interface to IP address mapping
# ip_dict = {
#     "GigabitEthernet0/1": "192.168.1.1/24",
#     "GigabitEthernet0/2": "192.168.2.1/24"
# }
#
# # Dictionary of interface to end device mapping
# device_dict = {
#     "GigabitEthernet0/1": "Server",
#     "GigabitEthernet0/2": "Printer"
# }
#
# # Get the configuration
# config = switch.get_config(ip_dict=ip_dict)
# print(config)

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

    def get_config(self, ip_dict, vlan_dict=None, vtp_domain=None, vtp_mode=None):
        config = self.generate_init_config(hostname=self.host_name, site=self.host_name[:2])

        # Add interface configurations
        for port in self.active_ports:
            if port.startswith("VLAN"):
                config += self.generate_vlan_config(port, vlan_dict)
                config += self.configure_vlan_interface(port, ip_dict)
            else:
                config += self.generate_physical_interface_config(port, ip_dict)

        # Configure VTP domain and mode if provided
        if vtp_domain:
            config += self.configure_vtp(vtp_domain, vtp_mode)

        return config

    @staticmethod
    def generate_vlan_config(vlan, vlan_dict=None):
        if vlan == "VLAN1" or not vlan_dict:
            return ""

        vlan_name = vlan_dict.get(vlan, f"VLAN {vlan}")
        return f'''
        vlan {vlan}
        name {vlan_name}
        exit
        '''

    def configure_vlan_interface(self, vlan, ip_dict=None):
        if vlan == "VLAN1" or not ip_dict or vlan not in ip_dict:
            return ""

        config = f'''
        interface vlan {vlan}
        '''

        ip_address = ip_dict[vlan]
        interface = self.convert_str_to_ipv4_interface(ip_address)
        config += f"ip address {interface.ip} {interface.netmask}\n"

        config += "\t\tno shutdown\n"
        config += "\t\texit\n"
        return config

    def generate_physical_interface_config(self, interface, ip_dict):
        config = f'''
        interface {interface}
        '''

        ip_address = ip_dict.get(interface)
        if ip_address:
            interface = self.convert_str_to_ipv4_interface(ip_address)
            config += f"ip address {interface.ip} {interface.netmask}\n"

        config += "\t\tno shutdown\n"
        config += "\t\texit\n"
        return config

    def configure_vtp(self, vtp_domain, vtp_mode=None):
        if vtp_mode:
            config = f'''
            vtp domain {vtp_domain}
            vtp mode {vtp_mode}
            exit
            '''
        else:
            config = f'''
            vtp domain {vtp_domain}
            exit
            '''

        return config

    @staticmethod
    def convert_str_to_ipv4_interface(ip_mask):
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

    def configure_routing_protocol(self):
        if self.routing_protocol == "OSPF":
            return self.configure_ospf()
        elif self.routing_protocol == "EIGRP":
            return self.configure_eigrp()
        else:
            return ""

    def configure_ospf(self):
        return '''
        router ospf 1
        network 0.0.0.0 255.255.255.255 area 0
        exit
        '''

    def configure_eigrp(self):
        return '''
        router eigrp 100
        network 0.0.0.0
        exit
        '''

    def generate_vlan_interface_config(self, vlan, ip_address):
        config = f'''
        interface vlan {vlan}
        ip address {ip_address}
        no shutdown
        exit
        '''
        return config

    def generate_config(self, ip_dict):
        config = super().generate_config(ip_dict)

        for vlan, ip_address in ip_dict.items():
            if vlan.startswith("VLAN") and self.check_vlan_interface(vlan):
                config += self.generate_vlan_interface_config(vlan, ip_address)

        return config

    def check_vlan_interface(self, vlan):
        for port in self.active_ports:
            if port.startswith("VLAN") and port == vlan:
                return True
        return False

    def get_full_config(self, ip_dict, vlan_dict=None, vtp_domain=None, vtp_mode=None):
        main_config = self.get_config(ip_dict=ip_dict, vlan_dict=vlan_dict, vtp_domain=vtp_domain, vtp_mode=vtp_mode)
        vlan_interface_config = self.generate_vlan_interface_configs(ip_dict=ip_dict)

        config = main_config + vlan_interface_config
        return config

    def generate_vlan_interface_configs(self, ip_dict):
        vlan_interface_configs = ""
        for port in self.active_ports:
            if port.startswith("VLAN") and port in ip_dict:
                vlan = port
                ip_address = ip_dict[port]
                vlan_interface_config = self.generate_vlan_interface_config(vlan, ip_address)
                vlan_interface_configs += vlan_interface_config

        return vlan_interface_configs

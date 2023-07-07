import ipaddress

class Switch:
    def __init__(self, model, host_name, ports, active_ports=None):
        self.model = model
        self.ports = ports
        self.active_ports = active_ports if active_ports is not None else []
        self.host_name = host_name
        self.subnet = "10.0.0.0/24"

    def get_active_ports(self):
        return self.active_ports

    # def set_active_ports(self, active_ports):
    #     self.active_ports = active_ports

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
    def set_active_ports(self, active_ports):
        self.active_ports = active_ports



        # Shut down all ports
        # for port in self.ports:
        #     config += f"interface {port}\n"
        #     config += "\t\tdown\n"
        #     config += "\t\texit\n"
        #
        # # Configure VLAN interfaces
        # for port in self.active_ports:
        #     if port.startswith("VLAN"):
        #         config += self.generate_vlan_interface_config(port)
        #
        # # Configure physical interfaces
        # for port in self.active_ports:
        #     if port.startswith("GigabitEthernet"):
        #         config += self.generate_physical_interface_config(port)


    def generate_vlan_interface_config(self, vlan):
        if vlan == "VLAN1":
            return ""

        vlan_name = vlan.lstrip("VLAN")
        ip_address = self.generate_ip_address(vlan_name)
        if ip_address:
            config = f'''
            interface {vlan}
            name VLAN {vlan_name}
            ip address {ip_address}
            no shutdown
            exit
            '''
            return config
        else:
            return ""

    def generate_physical_interface_config(self, interface):
        ip_address = self.generate_ip_address(interface)
        if ip_address:
            config = f'''
            interface {interface}
            ip address {ip_address}
            no shutdown
            exit
            '''
            return config
        else:
            return ""

    def generate_ip_address(self, name, prefix_length=24):
        subnet_ip = ipaddress.ip_network(self.subnet)
        for subnet in subnet_ip.subnets(new_prefix=prefix_length):
            if name in subnet.network_address.compressed:
                return self.get_next_ip_address(subnet)
        return ""

    def get_next_ip_address(self, subnet):
        try:
            return str(next(subnet.hosts()))
        except StopIteration:
            return ""

    # Rest of the class implementation...

    def get_config(self, ip_dict, vlan_dict=None, vtp_domain=None, vtp_mode=None):
        config = self.generate_init_config(hostname=self.host_name, site=self.host_name[:2])

        for port in self.active_ports:
            if port.startswith("VLAN"):
                config += self.generate_vlan_config(port, vlan_dict)
                config += self.configure_vlan_interface(port, ip_dict)
            else:
                config += self.generate_physical_interface_config(port, ip_dict)

        if vtp_domain:
            config += self.configure_vtp(vtp_domain, vtp_mode)

        return config

    # @staticmethod
    # def generate_vlan_config(vlan, vlan_dict=None):
    #     if vlan == "VLAN1" or not vlan_dict:
    #         return ""
    #
    #     vlan_name = vlan_dict.get(vlan, f"VLAN {vlan}")
    #     return f'''
    #     vlan {vlan}
    #     name {vlan_name}
    #     exit
    #     '''

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
    def generate_init_config(self,hostname, site, interface_range="GigabitEthernet0/0/0-24", static_pass="cisco",motd="Welcome to the Cisco network!"):
            config = f'''
           !{'=' * 40}!
           ! {hostname}{' ' * (39 - len(hostname))}!      
           !{'=' * 40}!  
    
           enable
           configure terminal
           no ip domain-lookup
           hostname {self.host_name}
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
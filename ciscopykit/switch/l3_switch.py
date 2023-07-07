from switch import Switch


class L3Switch(Switch):
    def __init__(self, model, ports, active_ports, routing_protocol):
        super().__init__(model, ports, active_ports)
        self.routing_protocol = routing_protocol

    # Rest of the class implementation...


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

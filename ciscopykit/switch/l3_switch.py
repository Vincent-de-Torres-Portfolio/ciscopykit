import ipaddress
from switch import Switch


class L3Switch(Switch):
    def __init__(self, model, ports, active_ports, routing_protocol, subnet):
        super().__init__(model, ports, active_ports)
        self.routing_protocol = routing_protocol
        self.subnet = subnet


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
        return """
        router ospf 1
        network 0.0.0.0 255.255.255.255 area 0
        exit
        """

    def configure_eigrp(self):
        return """
        router eigrp 100
        network 0.0.0.0
        exit
        """

    def generate_vlan_interface_config(self, vlan, ip,netmask):
        config = f"""
        interface vlan {(vlan.split('VLAN'))[1]}
        ip address {ip} {netmask}
        no shutdown
        exit
        """
        return config

    def generate_interface_config(self,interface, ip , netmask):
        config = f"""
        interface {interface}
        no switchport
        ip address {ip} {netmask}
        no shutdown
        exit
        """
        return config


    def generate_config(self, ip_dict,vtp_domain):
        config = self.generate_init_config(hostname=self.host_name, site=self.get_model()[:2])

        for interface, ip_address in ip_dict.items():
            ip_inf = ipaddress.IPv4Interface(ip_address)
            if interface.startswith("VLAN"):
                config += self.generate_vlan_interface_config(interface, ip_inf.ip ,ip_inf.netmask)
            else:
                config+= self.generate_interface_config(interface, ip_inf.ip ,ip_inf.netmask)
        config+= self.generate_vtp_config(vtp_domain)
        return config

    def generate_vtp_config(self, vtp_domain, vtp_mode='server'):
        config = f"""
        vtp domain {vtp_domain}
        vtp mode {vtp_mode}
        exit
        """
        return config

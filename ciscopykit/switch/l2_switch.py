from switch import Switch


class L2Switch(Switch):
    def __init__(self, model, ports, power_consumption, vlan_support):
        super().__init__(model, ports, power_consumption)
        self.vlan_support = vlan_support

    def get_vlan_support(self):
        return self.vlan_support

    def set_vlan_support(self, vlan_support):
        self.vlan_support = vlan_support

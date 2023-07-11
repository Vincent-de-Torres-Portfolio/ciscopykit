class VLANConfig:
    @staticmethod
    def create_vlan(vlan_id, vlan_name):
        """
        Create VLAN configuration.

        Args:
            vlan_id (int): VLAN ID.
            vlan_name (str): VLAN name.

        Returns:
            str: VLAN configuration.
        """
        config = f"""
vlan {vlan_id}
name {vlan_name}
"""
        interface_config = f"""
interface vlan {vlan_id}
no shutdown
exit"""
        return config, interface_config

    @staticmethod
    def configure_vtp_domain(vtp_domain):
        """
        Configure VTP domain.

        Args:
            vtp_domain (str): VTP domain name.

        Returns:
            str: VTP domain configuration.
        """
        return f"vtp domain {vtp_domain}"

    @staticmethod
    def configure_vtp_mode(vtp_mode):
        """
        Configure VTP mode.

        Args:
            vtp_mode (str): VTP mode.

        Returns:
            str: VTP mode configuration.
        """
        return f"vtp mode {vtp_mode}"

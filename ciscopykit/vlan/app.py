import argparse
from ciscopykit.vlan.vlan import VLANConfig

def create_vlan(args):
    """
    Create a VLAN.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        None
    """
    vlan_id = args.vlan_id
    vlan_name = args.vlan_name
    config, interface_config = VLANConfig.create_vlan(vlan_id, vlan_name)
    print(config)
    print(interface_config)

def configure_vtp_domain(args):
    """
    Configure the VTP domain.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        None
    """
    vtp_domain = args.vtp_domain
    config = VLANConfig.configure_vtp_domain(vtp_domain)
    print(config)

def configure_vtp_mode(args):
    """
    Configure the VTP mode.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        None
    """
    vtp_mode = args.vtp_mode
    config = VLANConfig.configure_vtp_mode(vtp_mode)
    print(config)

def main():
    """
    Main function to parse command-line arguments and execute corresponding subcommands.
    """
    parser = argparse.ArgumentParser(description='VLAN Subpackage')
    subparsers = parser.add_subparsers()

    # Create VLAN subcommand
    create_parser = subparsers.add_parser('create', help='Create a VLAN')
    create_parser.add_argument('vlan_id', type=int, help='VLAN ID')
    create_parser.add_argument('vlan_name', type=str, help='VLAN Name')
    create_parser.set_defaults(func=create_vlan)

    # Configure VTP domain subcommand
    configure_domain_parser = subparsers.add_parser('configure-domain', help='Configure VTP domain')
    configure_domain_parser.add_argument('vtp_domain', type=str, help='VTP Domain')
    configure_domain_parser.set_defaults(func=configure_vtp_domain)

    # Configure VTP mode subcommand
    configure_mode_parser = subparsers.add_parser('configure-mode', help='Configure VTP mode')
    configure_mode_parser.add_argument('vtp_mode', type=str, help='VTP Mode')
    configure_mode_parser.set_defaults(func=configure_vtp_mode)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()

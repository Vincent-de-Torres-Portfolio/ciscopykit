import argparse
from ciscopykit.lan_security.switchport_security import generate_switchport_security_config
from ciscopykit.lan_security.dhcp_snooping import generate_dhcp_snooping_config


def configure_switchport_security(args):
    """
    Generates and prints the switchport security configuration based on the provided arguments.

    Args:
        args (argparse.Namespace): Parsed arguments containing switchport security configuration details.

    """
    switchport_security_config = generate_switchport_security_config(
        args.interface, args.max_mac, args.violation_action, args.aging_time, not args.disable_sticky_mac
    )
    print(switchport_security_config)


def configure_dhcp_snooping(args):
    """
    Generates and prints the DHCP snooping configuration based on the provided arguments.

    Args:
        args (argparse.Namespace): Parsed arguments containing DHCP snooping configuration details.

    """
    dhcp_snooping_config = generate_dhcp_snooping_config(args.interface, args.trust_ports)
    print(dhcp_snooping_config)


def main():
    parser = argparse.ArgumentParser(description="LAN Security Configuration")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Subcommand: switchport_security
    switchport_security_parser = subparsers.add_parser("switchport_security")
    switchport_security_parser.add_argument(
        "interface", type=str, help="Interface name"
    )
    switchport_security_parser.add_argument(
        "max_mac", type=int, help="Maximum number of MAC addresses"
    )
    switchport_security_parser.add_argument(
        "--violation_action", choices=["restrict", "protect", "shutdown"], default="restrict",
        help="Violation action (default: restrict)"
    )
    switchport_security_parser.add_argument(
        "--aging_time", type=int, help="Aging time in minutes"
    )
    switchport_security_parser.add_argument(
        "--disable_sticky_mac", action="store_true", help="Disable sticky MAC address"
    )
    switchport_security_parser.set_defaults(func=configure_switchport_security)

    # Subcommand: dhcp_snooping
    dhcp_snooping_parser = subparsers.add_parser("dhcp_snooping")
    dhcp_snooping_parser.add_argument(
        "interface", type=str, help="Interface name"
    )
    dhcp_snooping_parser.add_argument(
        "trust_ports", nargs="+", type=str, help="List of trusted interface names"
    )
    dhcp_snooping_parser.set_defaults(func=configure_dhcp_snooping)

    args = parser.parse_args()

    # Call the corresponding function based on the selected subcommand
    if args.subcommand:
        args.func(args)
    else:
        parser.parse_args(["--help"])  # Display help for other subcommands


if __name__ == "__main__":
    main()

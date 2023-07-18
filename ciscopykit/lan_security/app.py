"""
LAN Security Configuration Tool

This tool provides a command-line interface for configuring various LAN security features. 
It supports the configuration of switchport security, DHCP snooping, Dynamic ARP Inspection 
(DAI), and VLAN security settings.

Usage:
    python app.py [subcommand] [arguments]

Subcommands:
    switchport_security  Configure switchport security settings.
    dhcp_snooping        Configure DHCP snooping settings.
    dai                  Configure Dynamic ARP Inspection (DAI) settings.
    vlan_security       Configure VLAN security settings.

For more information on each subcommand, use `python app.py [subcommand] --help`.
"""


import argparse
from ciscopykit.lan_security.switchport_security import generate_switchport_security_config
from ciscopykit.lan_security.dhcp_snooping import generate_dhcp_snooping_config
from ciscopykit.lan_security.dynamic_arp_inspection import generate_dai_config
from ciscopykit.lan_security.stp_security import configure_stp_security
from ciscopykit.lan_security.vlan_security import (
    configure_trunk_interfaces,
    configure_unused_ports,
    configure_access_ports,
)


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
    dhcp_snooping_config = generate_dhcp_snooping_config(
        args.interface, args.trust_ports)
    print(dhcp_snooping_config)


def configure_dai(args):
    """
    Generates and prints the Dynamic ARP Inspection (DAI) configuration based on the provided arguments.

    Args:
        args (argparse.Namespace): Parsed arguments containing DAI configuration details.
    """
    dai_config = generate_dai_config(args.interfaces, args.vlan)
    print(dai_config)


def configure_stp_sec(args):
    """
    Generates and prints the STP security configuration based on the provided arguments.

    Args:
        args (argparse.Namespace): Parsed arguments containing STP security configuration details.
    """
    stp_sec_config = configure_stp_security(args.interface)
    print(stp_sec_config)


def configure_vlan_security(args):
    """
    Configures VLAN security based on the provided arguments.

    Args:
        args (argparse.Namespace): Parsed arguments containing VLAN security configuration details.
    """
    if args.subcommand == "trunk_interfaces":
        trunk_interfaces_config = configure_trunk_interfaces(args.interface_range)
        print(trunk_interfaces_config)
    elif args.subcommand == "unused_ports":
        unused_ports_config = configure_unused_ports(args.interface_range, args.unused_vlan)
        print(unused_ports_config)
    elif args.subcommand == "access_ports":
        access_ports_config = configure_access_ports(args.interface_range)
        print(access_ports_config)


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

    # Subcommand: dai
    dai_parser = subparsers.add_parser("dai")
    dai_parser.add_argument(
        "interfaces", nargs="+", type=str, help="List of interfaces for Dynamic ARP Inspection"
    )
    dai_parser.add_argument(
        "--vlan", type=int, help="VLAN ID for DAI configuration"
    )
    dai_parser.set_defaults(func=configure_dai)

    # Subcommand: stp_sec
    stp_sec_parser = subparsers.add_parser("stp_sec")
    stp_sec_parser.add_argument(
        "interface", type=str, help="Interface name"
    )
    stp_sec_parser.set_defaults(func=configure_stp_sec)

    # Subcommand: vlan_security
    vlan_security_parser = subparsers.add_parser("vlan_security")
    vlan_security_subparsers = vlan_security_parser.add_subparsers(
        title="vlan_security_subcommands", dest="subcommand"
    )

    # Subcommand: vlan_security trunk_interfaces
    trunk_interfaces_parser = vlan_security_subparsers.add_parser("trunk_interfaces")
    trunk_interfaces_parser.add_argument(
        "interface_range", type=str, help="Range of interfaces (e.g., fa0/1 - 4)"
    )
    trunk_interfaces_parser.set_defaults(func=configure_vlan_security)

    # Subcommand: vlan_security unused_ports
    unused_ports_parser = vlan_security_subparsers.add_parser("unused_ports")
    unused_ports_parser.add_argument(
        "interface_range", type=str, help="Range of interfaces (e.g., fa0/5 - 10)"
    )
    unused_ports_parser.add_argument(
        "unused_vlan", type=int, help="VLAN ID for the unused ports"
    )
    unused_ports_parser.set_defaults(func=configure_vlan_security)

    # Subcommand: vlan_security access_ports
    access_ports_parser = vlan_security_subparsers.add_parser("access_ports")
    access_ports_parser.add_argument(
        "interface_range", type=str, help="Range of interfaces (e.g., fa0/11 - 24)"
    )
    access_ports_parser.set_defaults(func=configure_vlan_security)

    args = parser.parse_args()

    # Call the corresponding function based on the selected subcommand
    if args.subcommand:
        args.func(args)
    else:
        parser.parse_args(["--help"])  # Display help for other subcommands


if __name__ == "__main__":
    main()

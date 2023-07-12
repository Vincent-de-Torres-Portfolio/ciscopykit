
import argparse
import switchport_security


def configure_switchport_security(args):
    # Call the function from switchport_security.py
    switchport_security.configure_switchport_security(args.interface, args.max_mac, args.violation_action,
                                                      args.aging_time, not args.disable_sticky_mac)


def main():
    parser = argparse.ArgumentParser(description="LAN Security Configuration")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Subcommand: switchport_security
    switchport_security_parser = subparsers.add_parser("switchport_security")
    switchport_security_parser.add_argument(
        "interface", type=str, help="Interface name")
    switchport_security_parser.add_argument(
        "max_mac", type=int, help="Maximum number of MAC addresses")
    switchport_security_parser.add_argument("--violation_action", choices=["restrict", "protect", "shutdown"],
                                            default="restrict", help="Violation action (default: restrict)")
    switchport_security_parser.add_argument(
        "--aging_time", type=int, help="Aging time in minutes")
    switchport_security_parser.add_argument(
        "--disable_sticky_mac", action="store_true", help="Disable sticky MAC address")
    switchport_security_parser.set_defaults(func=configure_switchport_security)

    # Subcommands: Add other subcommands here

    args = parser.parse_args()

    # Call the corresponding function based on the selected subcommand
    if args.subcommand == "switchport_security":
        args.func(args)
    else:
        parser.parse_args(["--help"])  # Display help for other subcommands


if __name__ == "__main__":
    main()

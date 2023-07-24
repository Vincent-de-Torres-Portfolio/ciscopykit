"""
app.py - Command-line tool for configuring routing protocols.

This script provides a command-line interface to configure static routes and perform route redistribution for Cisco devices.
It uses the argparse module to parse command-line arguments and generate the corresponding configuration commands.

Usage:
    python app.py static --destination <destination> --next-hop <next_hop> [--admin-distance <distance>]
    python app.py redistribute --redistribute-protocol <protocol> [--ospf-id <ospf_id>] [--eigrp-as <eigrp_as>]

Arguments:
    static: Configure a static route on the device.
    redistribute: Perform route redistribution between routing protocols.

Options:
    --destination <destination>: The destination network address in CIDR notation (e.g., '10.10.10.0/24').
    --next-hop <next_hop>: The IP address of the next hop.
    --admin-distance <distance>: The administrative distance for the static route. Default is 1.

    --redistribute-protocol <protocol>: Specify the routing protocol for redistribution. Supported values are: 'rip', 'eigrp', 'ospf'.
    --ospf-id <ospf_id>: The OSPF process ID for redistribution (required if --redistribute-protocol is 'ospf').
    --eigrp-as <eigrp_as>: The EIGRP AS number for redistribution (required if --redistribute-protocol is 'eigrp').

Examples:
    python app.py static --destination 192.168.1.0/24 --next-hop 10.0.0.1 --admin-distance 5
    python app.py redistribute --redistribute-protocol ospf --ospf-id 1
    python app.py redistribute --redistribute-protocol eigrp --eigrp-as 100

This script uses the static_routing module from the ciscopykit.routing package to configure static routes
and perform route redistribution on Cisco devices.

"""

import argparse
from ciscopykit.routing import static_routing

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Routing Configuration")

# Add arguments for the routing protocol and its options
parser.add_argument("protocol", choices=[
                    "static", "redistribute"], help="Specify the routing protocol (static or redistribute)")
parser.add_argument(
    "--destination", help="The destination network address in CIDR notation (e.g., '10.10.10.0/24').")
parser.add_argument("--next-hop", help="The IP address of the next hop.")
parser.add_argument("--admin-distance", type=int, default=1,
                    help="The administrative distance for the static route. Default is 1.")
parser.add_argument("--redistribute-protocol", choices=[
                    "rip", "eigrp", "ospf"], help="Specify the routing protocol for redistribution.")
parser.add_argument("--ospf-id", type=int,
                    help="The OSPF process ID for redistribution.")
parser.add_argument("--eigrp-as", type=int,
                    help="The EIGRP AS number for redistribution.")

# Parse the command-line arguments
args = parser.parse_args()

if args.protocol == "static":
    if not args.destination or not args.next_hop:
        print("Error: Both --destination and --next-hop options are required for static route configuration.")
    else:
        static_route_config = static_routing.configure_static_route(
            args.destination, args.next_hop, args.admin_distance)
        print(static_route_config)
elif args.protocol == "redistribute":
    if not args.redistribute_protocol:
        print("Error: --redistribute-protocol option is required for route redistribution.")
    elif args.redistribute_protocol == "ospf" and not args.ospf_id:
        print("Error: --ospf-id option is required when --redistribute-protocol is 'ospf'.")
    elif args.redistribute_protocol == "eigrp" and not args.eigrp_as:
        print(
            "Error: --eigrp-as option is required when --redistribute-protocol is 'eigrp'.")
    else:
        redistribution_config = static_routing.configure_route_redistribution(
            args.redistribute_protocol, args.ospf_id, args.eigrp_as)
        print(redistribution_config)

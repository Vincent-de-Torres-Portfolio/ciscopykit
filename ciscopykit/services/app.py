import argparse
from dhcp_service import config_dhcp
from pat_service import config_pat

def parse_arguments():
    parser = argparse.ArgumentParser(description="Configure DHCP or PAT on a network device.")
    subparsers = parser.add_subparsers(title="services", dest="service")

    # DHCP subparser
    dhcp_parser = subparsers.add_parser("dhcp", help="Configure DHCP")
    dhcp_parser.add_argument("dhcp_pool_name", type=str, help="DHCP pool name")
    dhcp_parser.add_argument("network_address", type=str, help="Network address in CIDR format")
    dhcp_parser.add_argument("--dns_address", type=str, help="DNS address")
    dhcp_parser.add_argument("--dg", type=str, help="Default gateway address")
    dhcp_parser.add_argument("--exclude_ips", nargs=2, metavar=("min", "max"),
                             help="Excluded IP address range (min and max)")

    # PAT subparser
    pat_parser = subparsers.add_parser("pat", help="Configure PAT")
    pat_parser.add_argument("nat_inside_interface", type=str, help="Inside interface for NAT")
    pat_parser.add_argument("network_addresses", nargs="+", type=str, help="Network addresses to configure PAT for")
    pat_parser.add_argument("nat_outside_interface", type=str, help="Outside interface for NAT")
    pat_parser.add_argument("nat_pool_start", type=str, help="Start address of NAT pool")
    pat_parser.add_argument("nat_pool_end", type=str, help="End address of NAT pool")

    return parser.parse_args()

def run_dhcp_service(args):
    config = config_dhcp(args.dhcp_pool_name, args.network_address,
                         dns_address=args.dns_address, dg=args.dg, exclude_ips=args.exclude_ips)
    print(config)

def run_pat_service(args):
    config = config_pat(args.nat_inside_interface, args.network_addresses,
                        args.nat_outside_interface, args.nat_pool_start, args.nat_pool_end)
    print(config)

if __name__ == "__main__":
    args = parse_arguments()

    if args.service == "dhcp":
        run_dhcp_service(args)
    elif args.service == "pat":
        run_pat_service(args)
    else:
        print("Invalid service specified.")

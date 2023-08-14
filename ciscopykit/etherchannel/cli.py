import argparse
from ciscopykit.etherchannel.etherchannel import Layer2EtherChannel, Layer3EtherChannel

def configure_layer2(args):
    interfaces = args.interfaces.split(",")
    l2_etherchannel = Layer2EtherChannel(port_channel_number=args.port_channel_number, interfaces=interfaces, allowed_vlans=args.allowed_vlans)
    config = l2_etherchannel.configure()
    print(config)

def configure_layer3(args):
    interfaces = args.interfaces.split(",")
    l3_etherchannel = Layer3EtherChannel(port_channel_number=args.port_channel_number, interfaces=interfaces, ip_address=args.ip_address, subnet_mask=args.subnet_mask)
    config = l3_etherchannel.configure()
    print(config)

def main():
    parser = argparse.ArgumentParser(description="Configure Layer 2 and Layer 3 EtherChannels using CiscoPyKit.")
    subparsers = parser.add_subparsers(title="Subcommands", dest="subcommand")

    # Subparser for Layer 2 EtherChannel
    parser_layer2 = subparsers.add_parser("layer2", help="Configure Layer 2 EtherChannel")
    parser_layer2.add_argument("port_channel_number", type=int, help="Port channel number")
    parser_layer2.add_argument("interfaces", help="Comma-separated list of interfaces")
    parser_layer2.add_argument("--allowed_vlans", help="VLANs allowed on the trunk interface")

    # Subparser for Layer 3 EtherChannel
    parser_layer3 = subparsers.add_parser("layer3", help="Configure Layer 3 EtherChannel")
    parser_layer3.add_argument("port_channel_number", type=int, help="Port channel number")
    parser_layer3.add_argument("interfaces", help="Comma-separated list of interfaces")
    parser_layer3.add_argument("ip_address", help="IP address for the EtherChannel")
    parser_layer3.add_argument("subnet_mask", help="Subnet mask for the EtherChannel")

    args = parser.parse_args()

    if args.subcommand == "layer2":
        configure_layer2(args)
    elif args.subcommand == "layer3":
        configure_layer3(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

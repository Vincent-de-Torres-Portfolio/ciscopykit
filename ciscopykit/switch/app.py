import argparse
from l3_switch import L3Switch


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="L3 Switch Configuration")

    # Add arguments
    parser.add_argument("--model", required=True, help="Switch model")
    parser.add_argument("--ports", required=True, help="List of switch ports")
    parser.add_argument("--active-ports", required=True, help="List of active switch ports")
    parser.add_argument("--routing-protocol", required=True, help="Routing protocol")
    parser.add_argument("--ip-dict", help="Dictionary of VLAN IP addresses")
    parser.add_argument("--hostname", required=True, help="Switch hostname")
    parser.add_argument("--subnet", required=True, help="Subnet for IP address generation")
    parser.add_argument("--save-config", help="File path to save the configuration")
    parser.add_argument("--vtp-domain", help="Assign VTP Domain.")



    # Parse the command-line arguments
    args = parser.parse_args()

    # Extract the values from the arguments
    model = args.model
    ports = args.ports.split(",")
    active_ports = args.active_ports.split(",")
    routing_protocol = args.routing_protocol
    ip_dict = eval(args.ip_dict) if args.ip_dict else {}
    hostname = args.hostname
    subnet = args.subnet
    save_config = args.save_config
    vtp_domain=args.vtp_domain

    # Create an instance of the L3Switch class
    l3_switch = L3Switch(model, ports, active_ports, routing_protocol, subnet=subnet)

    # Set the hostname and subnet
    l3_switch.host_name = hostname
    l3_switch.subnet = subnet

    # Generate the configuration
    config = l3_switch.generate_config(ip_dict,vtp_domain)

    # Clean the configuration by stripping whitespaces
    config = config.strip()

    # Print the configuration
    print("Generated Configuration:")
    print(config)

    # Save the configuration to a file if specified
    if save_config:
        with open(save_config, "w") as file:
            config_list = config.split('\n')
            config_list = [each.strip() for each in config_list]
            for each in config_list:
                file.write(each + '\n')

        print(f"Configuration saved to {save_config}")


if __name__ == "__main__":
    main()

# python app.py --model "Cisco 3750" --ports "GigabitEthernet1/0/1,GigabitEthernet1/0/2,VLAN10,VLAN20" --
# active-ports "GigabitEthernet1/0/1,GigabitEthernet1/0/2" --routing-protocol "OSPF" --ip-dict "{'VLAN10': '10.0.0.1/24', 'VLAN20': '20.0.0.1/24', 'Gi0/0':'10.10.11.1/30'}" --hostname "LA_SW1" --subnet "10.0.0.0/16" --save-config ./config.txt
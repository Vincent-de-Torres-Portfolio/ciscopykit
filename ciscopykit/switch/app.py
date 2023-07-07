import argparse
from switch import Switch

def main():
    parser = argparse.ArgumentParser(description="L3 Switch Configuration Demo")
    parser.add_argument("--model", type=str, help="Switch model")
    parser.add_argument("--ports", type=str, help="Comma-separated list of switch ports")
    parser.add_argument("--active_ports", type=str, help="Comma-separated list of active switch ports")
    parser.add_argument("--routing_protocol", type=str, help="Routing protocol (OSPF or EIGRP)")
    parser.add_argument("--vlan_dict", type=str, help="Dictionary of VLAN names (optional)")
    parser.add_argument("--ip_dict", type=str, help="Dictionary of IP addresses for interfaces")
    parser.add_argument("--vtp_domain", type=str, help="VTP domain name")
    parser.add_argument("--vtp_mode", type=str, help="VTP mode (optional)")

    args = parser.parse_args()

    model = args.model
    ports = args.ports.split(",")
    active_ports = args.active_ports.split(",")
    routing_protocol = args.routing_protocol
    vlan_dict = eval(args.vlan_dict) if args.vlan_dict else None
    ip_dict = eval(args.ip_dict) if args.ip_dict else {}
    vtp_domain = args.vtp_domain
    vtp_mode = args.vtp_mode

    l3_switch = Switch(model, "MySwitch", ports)

    l3_switch.set_active_ports(active_ports)

    config = l3_switch.generate_init_config(hostname=l3_switch.host_name, site=l3_switch.host_name[:2])

    # Configure VLAN interfaces
    for port in active_ports:
        if port.startswith("VLAN") and port in ip_dict:
            vlan = port
            ip_address = ip_dict[port]
            config += f"interface {vlan}\n"
            config += f"   ip address {ip_address}\n"
            config += "   no shutdown\n"
            config += "   exit\n"

    # Configure physical interfaces
    for port in active_ports:
        if port.startswith("GigabitEthernet") and port in ip_dict:
            interface = port
            ip_address = ip_dict[port]
            config += f"interface {interface}\n"
            config += f"   ip address {ip_address}\n"
            config += "   no shutdown\n"
            config += "   exit\n"

    # Configure VTP
    if vtp_domain:
        config += f"vtp domain {vtp_domain}\n"
        if vtp_mode:
            config += f"vtp mode {vtp_mode}\n"
        config += "exit\n"

    # Print the switch configuration
    print(config)


if __name__ == "__main__":
    main()

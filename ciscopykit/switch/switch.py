import argparse
from app import Switch

# Create an argument parser
parser = argparse.ArgumentParser(description='Switch Configuration')

# Add arguments
parser.add_argument('--model', type=str, help='Switch model')
parser.add_argument('--hostname', type=str, help='Switch hostname')
parser.add_argument('--ports', nargs='+', help='Switch ports')
parser.add_argument('--active-ports', nargs='+', help='Active ports')
parser.add_argument('--ip-dict', type=str, help='Interface to IP address mapping')

# Parse the arguments
args = parser.parse_args()

# Create a Switch object
switch = Switch(model=args.model, host_name=args.hostname, ports=args.ports)

# Set the active ports
switch.set_active_ports(args.active_ports)

# Parse the IP dictionary string into a dictionary
ip_dict = {}
if args.ip_dict:
    ip_dict_str = args.ip_dict.split(',')
    for entry in ip_dict_str:
        interface, ip_address = entry.split(':')
        ip_dict[interface] = ip_address

# Get the configuration
config = switch.get_config(ip_dict=ip_dict)
print(config)


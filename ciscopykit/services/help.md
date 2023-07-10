
# CiscoPyKit `services` Package

The CiscoPyKit Services Configuration package provides submodules for configuring network services such as DHCP and PAT. This package allows you to easily configure network settings on Cisco network devices.

## Installation

You can install the CiscoPyKit Network Configuration package using pip:

```
pip install ciscopykit
```

## Usage

The package provides a command-line interface (CLI) that uses argparse to configure network services. Here's how you can use the package with argparse:

### DHCP Configuration

To configure DHCP on a Cisco network device, use the following command:

```
python -m ciscopykit.services.app dhcp <dhcp_pool_name> <network_address> [--dns_address <dns_address>] [--dg <default_gateway>] [--exclude_ips <min> <max>]
```

- `<dhcp_pool_name>`: The name of the DHCP pool.
- `<network_address>`: The network address in CIDR format.
- `--dns_address <dns_address>` (optional): The DNS address for the DHCP clients.
- `--dg <default_gateway>` (optional): The default gateway address.
- `--exclude_ips <min> <max>` (optional): The range of IP addresses to exclude from the DHCP pool.

Example usage:

```
python -m ciscopykit.services.app dhcp V10 "10.3.28.0/22" --dns_address "10.3.20.100" --exclude_ips "10.3.30.1" "10.3.30.100"
```

This will generate the DHCP configuration for the specified parameters.

### PAT Configuration

To configure Port Address Translation (PAT) on a Cisco network device, use the following command:

```
python -m ciscopykit.services.app pat <nat_inside_interface> <network_address1> <network_address2> ... <nat_outside_interface> <nat_pool_start> <nat_pool_end>
```

- `<nat_inside_interface>`: The inside interface for NAT.
- `<network_address1> <network_address2> ...`: The network addresses to configure PAT for.
- `<nat_outside_interface>`: The outside interface for NAT.
- `<nat_pool_start>`: The start address of the NAT pool.
- `<nat_pool_end>`: The end address of the NAT pool.

Example usage:

```
python -m ciscopykit.services.app pat eth0 "192.168.0.0/24" "10.0.0.0/16" eth1 "192.0.2.1" "192.0.2.100"
```

This will generate the PAT configuration for the specified parameters.

---
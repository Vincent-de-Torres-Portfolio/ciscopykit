# CiscoPyKit GRE Module

The CiscoPyKit GRE module provides a Python script to configure Generic Routing Encapsulation (GRE) tunnels for Cisco routers. This module allows users to easily generate GRE tunnel configurations by providing the necessary parameters through the command line.

## Installation

This module is a part of the CiscoPyKit package. To install CiscoPyKit, you can use pip:

```bash
pip install ciscopykit
```

## Usage

The GRE module can be used to generate GRE tunnel configurations by specifying the tunnel ID, tunnel source, tunnel destination, and optional tunnel IP address.

```bash
python -m ciscopykit.gre <tunnel_id> <tunnel_source> <tunnel_destination> [--tunnel_ip]
```

Arguments:
- `tunnel_id`: The ID of the GRE tunnel (1 to 65535).
- `tunnel_source`: The source IP address of the GRE tunnel.
- `tunnel_destination`: The destination IP address of the GRE tunnel.
- `--tunnel_ip`: Optional IP address to assign to the GRE tunnel interface.

Example:

```bash
python -m ciscopykit.gre 1 10.0.0.1 20.0.0.1 --tunnel_ip 192.168.0.1
```

## Output

The script will output the corresponding GRE tunnel configuration that can be directly copied and pasted into a Cisco router's IOS configuration.

## Contributing

Contributions to the CiscoPyKit project are welcome! Feel free to open issues for bugs, feature requests, or to submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

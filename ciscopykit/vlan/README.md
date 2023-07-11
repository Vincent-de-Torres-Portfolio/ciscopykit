# **`vlan` package**

The VLAN subpackage provides functionality for creating VLANs and configuring VTP (VLAN Trunking Protocol) settings.

## Installation

You can use the VLAN subpackage installing ciscopykit using pip:

```shell
pip install ciscopykit
```

---

## Usage

### Creating VLANs

To create a VLAN, use the `create` command followed by the VLAN ID and VLAN name:

```shell
vlan create <vlan_id> <vlan_name>
```

Example:
```shell
vlan create 10 "mgt"
```

This command will create a VLAN with the specified VLAN ID and VLAN name.

### Configuring VTP Domain

To configure the VTP domain, use the `configure-domain` command followed by the VTP domain name:

```shell
vlan configure-domain <vtp_domain>
```

Example:
```shell
vlan configure-domain "example-domain"
```

This command will configure the VTP domain with the specified name.

### Configuring VTP Mode

To configure the VTP mode, use the `configure-mode` command followed by the VTP mode:

```shell
vlan configure-mode <vtp_mode>
```

Example:
```shell
vlan configure-mode "server"
```

This command will configure the VTP mode with the specified mode.

## Contributing

Contributions to the VLAN subpackage are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This VLAN subpackage is open-source and is distributed under the [MIT License](LICENSE.md).

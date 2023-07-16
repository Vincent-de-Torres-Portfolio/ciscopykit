# LAN Security Package

The LAN Security package provides a collection of modules and functions that assist in configuring various security features and settings for local area networks (LANs). These security measures are designed to protect network infrastructure, prevent unauthorized access, and mitigate potential security risks.

## `switchport_security` module

The `configure_switchport_security` function is a part of the LAN Security module and is used to generate the configuration command for switchport security. This function allows for easy configuration of various security settings on switchports to enhance network security and prevent unauthorized access.

## Function Signature
```python
def configure_switchport_security(interface, max_mac, violation_action='restrict', aging_time=None, sticky_mac=True):
```

### Parameters
- `interface` (str): The name of the interface on which switchport security will be configured.
- `max_mac` (int): The maximum number of MAC addresses allowed to be learned on the interface.
- `violation_action` (str, optional): The violation action to be taken when the maximum number of MAC addresses is exceeded. It can be set to `'restrict'`, `'protect'`, or `'shutdown'`. The default value is `'restrict'`.
- `aging_time` (int, optional): The aging time for dynamically learned secure MAC addresses in minutes. If not specified, the aging time is not configured.
- `sticky_mac` (bool, optional): Specifies whether to enable sticky MAC address. If set to `True`, the switch will learn and retain MAC addresses dynamically. If set to `False`, sticky MAC address is disabled. The default value is `True`.

### Returns
- `str`: The configuration command for switchport security.

### Exceptions
- `ValueError`: Raised when the `violation_action` parameter is not one of `'restrict'`, `'protect'`, or `'shutdown'`.

## Usage Examples
The `configure_switchport_security` function can be used in various scenarios to configure switchport security. Here are some usage examples:

### Example 1: Basic Configuration
```python
interface = "GigabitEthernet1/0/1"
max_mac = 5
config = configure_switchport_security(interface, max_mac)
print(config)
```
Output:
```
interface GigabitEthernet1/0/1
switchport mode access
switchport port-security
switchport port-security maximum 5
switchport port-security violation restrict
switchport port-security mac-address sticky
```

### Example 2: Custom Violation Action and Aging Time
```python
interface = "GigabitEthernet1/0/2"
max_mac = 10
violation_action = "protect"
aging_time = 120
config = configure_switchport_security(interface, max_mac, violation_action, aging_time)
print(config)
```
Output:
```
interface GigabitEthernet1/0/2
switchport mode access
switchport port-security
switchport port-security maximum 10
switchport port-security violation protect
switchport port-security aging time 120
switchport port-security mac-address sticky
```

### Example 3: Disable Sticky MAC Address
```python
interface = "GigabitEthernet1/0/3"
max_mac = 5
sticky_mac = False
config = configure_switchport_security(interface, max_mac, sticky_mac=sticky_mac)
print(config)
```
Output:
```
interface GigabitEthernet1/0/3
switchport mode access
switchport port-security
switchport port-security maximum 5
switchport port-security violation restrict
```

### Example 4: Invalid Violation Action (Raises ValueError)
```python
interface = "GigabitEthernet1/0/4"
max_mac = 5
violation_action = "invalid_action"
config = configure_switchport_security(interface, max_mac, violation_action)
```
Output:
```
ValueError: Invalid violation action. It must be 'restrict', 'protect', or 'shutdown'.
```

## `dhcp_snooping` module

The `generate_dhcp_snooping_config` function in the `dhcp_snooping` module is part of the LAN Security package. It enables you to generate the configuration commands for DHCP snooping on Cisco IOS devices. DHCP snooping is a security feature that prevents unauthorized DHCP servers from providing IP configuration to network clients and mitigates potential DHCP-related attacks.

### Function Signature

```python
def generate_dhcp_snooping_config(interface, trust_ports=None):
```

#### Parameters

- `interface` (str): The name of the interface on which DHCP snooping will be enabled.
- `trust_ports` (list or None, optional): A list of interface names to be trusted by DHCP snooping. If provided, DHCP snooping will not inspect DHCP traffic on these trusted ports. If not specified or set to `None`, all ports except the interface specified will be trusted.

#### Returns

- `str`: The configuration commands for DHCP snooping.

### Usage Example

Here's an example of using the `generate_dhcp_snooping_config` function to configure DHCP snooping:

```python
interface = "GigabitEthernet1/0/1"
trust_ports = ["GigabitEthernet1/0/2", "GigabitEthernet1/0/3"]
config = generate_dhcp_snooping_config(interface, trust_ports)
print(config)
```

**Output:**

```
ip dhcp snooping
!
interface GigabitEthernet1/0/1
  ip dhcp snooping trust
!
interface GigabitEthernet1/0/2
  ip dhcp snooping trust
!
interface GigabitEthernet1/0/3
  ip dhcp snooping trust
```

In this example, the `generate_dhcp_snooping_config` function is called with the interface `"GigabitEthernet1/0/1"` and a list of trusted ports `["GigabitEthernet1/0/2", "GigabitEthernet1/0/3"]`. The function generates the DHCP snooping configuration commands, which include enabling DHCP snooping globally and trusting the specified interface and ports.

## `dynamic_arp_inspection` module

The `generate_dai_config` function in the `dynamic_arp_inspection` module is part of the LAN Security package. It allows you to generate the configuration commands for Dynamic ARP Inspection (DAI) on Cisco IOS devices. DAI validates ARP packets on the network, protecting against ARP spoofing and other ARP-based attacks.

### Function Signature

```python
def generate_dai_config(interfaces):
```

#### Parameters

- `interfaces` (list): A list of interfaces on which Dynamic ARP Inspection (DAI) should be enabled.

#### Returns

- `str`: The configuration commands for DAI.

### Usage Example

Here's an example of using the `generate_dai_config` function to configure Dynamic ARP Inspection (DAI):

```python
interfaces = ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2", "GigabitEthernet1/0/3"]
config = generate_dai_config(interfaces)
print(config)
```

**Output:**

```
ip arp inspection
!
interface GigabitEthernet1/0/1
ip arp inspection trust
!
interface GigabitEthernet1/0/2
ip arp inspection trust
!
interface GigabitEthernet1/0/3
ip arp inspection trust
```

## `stp_security` module

The `configure_stp_security` function in the LAN Security package is used to configure PortFast and BPDU Guard on the specified interface. This function ensures enhanced security and prevents unauthorized access on the network.

## Function Signature

```python
def configure_stp_security(interface):
```

#### Parameters

- `interface` (str): The name of the interface on which to configure PortFast and BPDU Guard.

#### Returns

- `str`: The configuration commands for enabling PortFast and BPDU Guard on the interface.

#### Raises

- `ValueError`: If the interface name is not valid.

## Usage Example

Here's an example of using the `configure_stp_security` function to configure PortFast and BPDU Guard on an interface:

```python
interface = "GigabitEthernet1/0/1"
config = configure_stp_security(interface)
print(config)
```

**Output:**

```
spanning-tree portfast default
interface GigabitEthernet1/0/1
spanning-tree bpduguard enable
```
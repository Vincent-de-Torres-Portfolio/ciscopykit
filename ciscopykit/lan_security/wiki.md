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


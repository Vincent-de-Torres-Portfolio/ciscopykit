# LAN Security

## switchport_security.py

The `switchport_security` module provides a function for generating the configuration command for switchport security.

### Usage

#### Case 1: Basic configuration
```
# Assuming proper module imports

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

#### Case 2: Custom violation action and aging time
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

#### Case 3: Disable sticky MAC address
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

#### Case 4: Invalid violation action (raises ValueError)
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
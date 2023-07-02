# `device.py`

Represents a network device.

## Attributes

- `device_type (str)`: The type of the device.
- `hostname (str)`: The hostname of the device.
- `site (str)`: The site name of the device.
- `fqdn (str)`: The fully qualified domain name of the device.
- `active_interfaces (list)`: The list of active interfaces.
- `layer (str)`: The layer of the device (Core, Distribution, Access).

## Methods

### `__init__(self, device_type, hostname, site, layer)`

Initializes a Device object.

#### Arguments

- `device_type (str)`: The type of the device.
- `hostname (str)`: The hostname of the device.
- `site (str)`: The site name of the device.
- `layer (str)`: The layer of the device (Core, Distribution, Access).

### `modify_hostname(self, new_hostname)`

Modifies the hostname of the device.

#### Arguments

- `new_hostname (str)`: The new hostname of the device.

### `modify_site(self, new_site)`

Modifies the site name of the device.

#### Arguments

- `new_site (str)`: The new site name of the device.

### `remove_attribute(self, attribute_name)`

Removes an attribute from the device.

#### Arguments

- `attribute_name (str)`: The name of the attribute to remove.

### `add_interface(self, interface)`

Adds an interface to the device.

#### Arguments

- `interface (Interface)`: The interface to add.

### `remove_interface(self, interface)`

Removes an interface from the device.

#### Arguments

- `interface (Interface)`: The interface to remove.

### `update_fqdn(self)`

Updates the fully qualified domain name based on the hostname and site 
name.

### `extract_hostname_site(fqdn)`

Extracts the hostname and site name from a fully qualified domain name.

#### Arguments

- `fqdn (str)`: The fully qualified domain name.

#### Returns

- `tuple`: A tuple containing the hostname and site name.

#### Raises

- `ValueError`: If the fully qualified domain name is invalid.

### `get_active_interfaces(self)`

Returns the list of active interfaces.

#### Returns

- `list`: The list of active interfaces.

## Usage

### Creating a Device object

To create a new device object, you can use the `Device` constructor as 
follows:

```python
device = Device(device_type="Router", hostname="router1", site="site1", 
layer="Core")
```

This will create a device of type "Router" with the hostname "router1", 
site name "site1", and it will be assigned to the "Core" layer.

### Modifying the hostname and site name

You can modify the hostname and site name of a device using the 
`modify_hostname` and `modify_site` methods, respectively:

```python
device.modify_hostname("new_router1")
device.modify_site("new_site1")
```

### Adding and removing interfaces

To add an interface to a device, you can use the `add_interface` method:

```python
interface = Interface(name="GigabitEthernet0/0", ip_address="192.168.1.1")
device.add_interface(interface)
```

To remove an interface from a device, use the `remove_interface` method:

```python
device.remove_interface(interface)
```

### Updating the fully qualified domain name

You can update the fully qualified domain name of a

 device based on its hostname and site name using the `update_fqdn` 
method:

```python
device.update_fqdn()
```

### Extracting hostname and site name from FQDN

If you have a fully qualified domain name and you want to extract the 
hostname and site name, you can use the `extract_hostname_site` method:

```python
fqdn = "new_router1.new_site1.example.com"
hostname, site = Device.extract_hostname_site(fqdn)
```

### Retrieving active interfaces

To retrieve the list of active interfaces for a device, use the 
`get_active_interfaces` method:

```python
active_interfaces = device.get_active_interfaces()
```

This will return a list of active interface objects.




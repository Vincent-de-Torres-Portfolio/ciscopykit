# Router Configuration Generator Demo

This demo showcases a simple router configuration generator that creates a router configuration based on input parameters and writes it to a file. It utilizes the `ciscopykit` library, which can be installed via pip.

## Prerequisites
- Python 3.x installed on your system.
- The `ciscopykit` library is required. You can install it using `pip install ciscopykit`.

## How to Run the Demo
1. Make sure you have met the prerequisites mentioned above.
2. Copy and paste the provided code into a Python environment or a Python script file (e.g., `router_config_generator.py`).
3. Import the necessary classes from the `ciscopykit.device` module.
4. Customize the input parameters as per your requirements:
    - `hostname`: The desired hostname for the router.
    - `ip_network`: The IP network in CIDR notation (e.g., "192.168.1.0/24") representing the network the router is connected to.
    - `interfaces`: A list of dictionaries, where each dictionary represents an interface configuration. Each dictionary should contain the following keys:
        - `'name'`: The name of the interface (e.g., 'g0/0', 'g0/1').
        - `'ip'`: An `ipaddress.IPv4Interface` object representing the IP address and subnet mask of the interface.
5. Run the script using `python router_config_generator.py` or execute the code in your Python environment.

## Output
- The script will generate a router configuration based on the provided input parameters.
- The generated configuration will be saved to a file named `router-config.txt` in the current directory.
- A success message will be displayed indicating that the configuration file has been generated successfully.

Please note that the code assumes the existence of the necessary classes from the `ciscopykit.device` module with their respective methods. Ensure that the `ciscopykit` library is correctly installed to avoid any import errors.

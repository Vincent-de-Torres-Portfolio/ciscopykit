# L3 Switch Configuration

This package provides a command-line interface for generating and configuring L3 switch settings. It utilizes the `argparse` module to parse command-line arguments and the `l3_switch` module to generate the switch configuration.

## Prerequisites
- Python 3.x

## Installation
1. Clone or download the repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage
To generate and configure the L3 switch, execute the following command in your terminal:

```shell
python app.py --model "<switch_model>" --ports "<port_list>" --active-ports "<active_port_list>" --routing-protocol "<protocol>" --ip-dict "<ip_dictionary>" --hostname "<switch_hostname>" --subnet "<subnet>" --save-config "<config_file_path>"

```

### Arguments
- `--model`: Specifies the switch model.
- `--ports`: Specifies a comma-separated list of all switch ports.
- `--active-ports`: Specifies a comma-separated list of active switch ports.
- `--routing-protocol`: Specifies the routing protocol to be used.
- `--ip-dict`: (Optional) Provides a dictionary of VLAN IP addresses.
- `--hostname`: Specifies the hostname of the switch.
- `--subnet`: Specifies the subnet for IP address generation.
- `--save-config`: (Optional) Specifies the file path to save the configuration.

**Note:** Replace the placeholders (`<switch_model>`, `<port_list>`, `<active_port_list>`, `<protocol>`, `<ip_dictionary>`, `<switch_hostname>`, `<subnet>`, and `<config_file_path>`) with appropriate values.

### Example
```shell
python app.py --model "Cisco 3750" --vtp-domain "LA" --ports "GigabitEthernet1/0/1,GigabitEthernet1/0/2,VLAN10,VLAN20" --active-ports "GigabitEthernet1/0/1,GigabitEthernet1/0/2" --routing-protocol "OSPF" --ip-dict "{'VLAN10': '10.0.0.1/24', 'VLAN20': '20.0.0.1/24', 'Gi0/0':'10.10.11.1/30'}" --hostname "LA_SW1" --subnet "10.0.0.0/16" --save-config ./config.txt
```
### Output

```plaintext
Generated Configuration:
!========================================!
! LA_SW1                                 !
!========================================!

enable
configure terminal
no ip domain-lookup
hostname LA_SW1
username admin secret cisco

line console 0
logging synchronous
exit
conf t
ip domain-name Ci.ccna.com
crypto key generate rsa
1024

banner motd $Welcome to the Cisco network!$
enable secret cisco
line console 0
password cisco
login
exit

line vty 0 4
login local
transport input ssh
ip ssh version 2

service password-encryption

interface vlan 10
ip address 10.0.0.1 255.255.255.0
no shutdown
exit

interface vlan 20
ip address 20.0.0.1 255.255.255.0
no shutdown
exit

interface Gi0/0
no switchport
ip address 10.10.11.1 255.255.255.252
no shutdown
exit

vtp domain LA
vtp mode server
exit

!========================================!
!   Configuration saved to ./config.txt  !
!========================================!


```
## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
This project utilizes the `argparse` module and the `l3_switch` module for generating the L3 switch configuration.
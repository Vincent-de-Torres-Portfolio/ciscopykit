from ipaddress import IPv4Address, IPv4Network
def config_pat(nat_inside_interface, network_addresses, nat_outside_interface, nat_pool_start, nat_pool_end):
    """
    Configures Port Address Translation (PAT) on a network device.
    :param nat_inside_interface: str
    :param network_addresses: list[str]
    :param nat_outside_interface: str
    :param nat_pool_start: str
    :param nat_pool_end: str
    :return: str
    """

    nat_poolname = 'NAT_POOL'

    nat_pool_min = IPv4Address(nat_pool_start)
    nat_pool_max = IPv4Address(nat_pool_end)

    str_to_return = f"""

interface {nat_inside_interface}
ip nat inside
interface {nat_outside_interface}
ip nat outside
ip nat pool {nat_poolname} {nat_pool_min} {nat_pool_max} netmask 255.255.255.0

"""

    for network_address in network_addresses:
        network = IPv4Network(network_address)
        nat_acl_id = f'{network_address}-NAT-ACL'

        str_to_return += f"""

ip access-list standard {nat_acl_id}
permit {network}
ip nat inside source list {nat_acl_id} pool {nat_poolname} overload


"""

    return str_to_return
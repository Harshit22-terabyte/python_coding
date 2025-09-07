
'''

def ip_to_binary(ip):
    """
    Converts a dotted-decimal IP address (e.g., '192.168.1.10') into a 32-bit binary string.
    """
    return ''.join([f"{int(octet):08b}" for octet in ip.split('.')])

def cidr_to_subnet_mask(prefix_length):
    """
    Converts a prefix length (e.g., 24) into a dotted-decimal subnet mask (e.g., '255.255.255.0').
    """
    mask = (1 << 32) - (1 << 32 - prefix_length)  # Create a full subnet mask of `prefix_length` ones
    mask_octets = [(mask >> i) & 0xFF for i in (24, 16, 8, 0)]  # Split into 4 8-bit octets
    return '.'.join(map(str, mask_octets))

def check_ip_in_subnet(ip, network, prefix_length):
    """
    Checks if the given IP address belongs to the subnet defined by the network and prefix.
    """
    # Convert inputs to binary
    ip_bin = ip_to_binary(ip)
    subnet_bin = ip_to_binary(network)
    mask_bin = ip_to_binary(cidr_to_subnet_mask(prefix_length))

    # Calculate network address using bitwise AND
    network_address = ''.join([str(int(subnet_bin[i]) & int(mask_bin[i])) for i in range(32)])
    ip_network_address = ''.join([str(int(ip_bin[i]) & int(mask_bin[i])) for i in range(32)])

    # Compare
    return network_address == ip_network_address

# Testing the function
ip = "192.168.1.10"
network = "192.168.1.0"
prefix_length = 24

if check_ip_in_subnet(ip, network, prefix_length):
    print(f"The IP address {ip} belongs to the subnet {network}/{prefix_length}.")
else:
    print(f"The IP address {ip} does NOT belong to the subnet {network}/{prefix_length}.")'''
	
	
	
'''

import ipaddress

def is_ip_in_subnet(ip, subnet):
    try:
        # Convert the IP address and subnet to objects
        ip_obj = ipaddress.ip_address(ip)
        subnet_obj = ipaddress.ip_network(subnet, strict=False) 

        # Check if the IP address is in the subnet
        return ip_obj in subnet_obj
    except ValueError:
        # Handle invalid IP or subnet inputs
        return False

# Test the function
ip = "192.168.1.100"
subnet = "192.168.1.0/24"  # Subnet in CIDR notation
result = is_ip_in_subnet(ip, subnet)

if result:
    print(f"The IP address {ip} belongs to the subnet {subnet}.")
else:
    print(f"The IP address {ip} does NOT belong to the subnet {subnet}.")
	
'''
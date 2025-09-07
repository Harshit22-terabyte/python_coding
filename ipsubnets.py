import ipaddress
address=ipaddress.ip_address("192.168.1.12")
network=ipaddress.ip_network("192.168.1.0/24")


"""def is_ip_in_subnet(ip, subnet):
    try:
        # Convert the IP address and subnet to objects
        ip_obj = ipaddress.ip_address(ip)
        subnet_obj = ipaddress.ip_network(subnet, strict=False) 

        # Check if the IP address is in the subnet
        return ip_obj in subnet_obj
    except ValueError:
        # Handle invalid IP or subnet inputs
        return False"""

result=address in network

print(result)

"""
Steps to Check if an IP is in a Subnet:
1.Convert the IP address and subnet mask from dot-decimal notation to binary.
2.Compute the network address using a bitwise AND operation between the IP and the subnet mask.
3.Compute the network range for the subnet (start of the range = network address, end of the range = broadcast address).
4.Check if the given IP falls within this range.

"""


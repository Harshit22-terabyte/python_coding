"""
Padding scenerio for decimal to binary"""

max_num = 15  # Assume highest decimal value is 15
required_bits = max_num.bit_length()  # Output: 4 (because 15 requires 4 bits)
padded_binary = bin(2)[2:].zfill(required_bits)
print(padded_binary)  # Output: '0010'




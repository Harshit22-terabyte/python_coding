"""convert dec to binary"""
decimal=25
binary=bin(decimal).replace("0b","")
print("Binary value of 25 is",bin(decimal).replace("0b",""), end="\n",sep=" : ")

"""convert dec to hex"""
print("Hexadecimal value of 25 is",hex(decimal).replace("0x",""))
hexadecimal=hex(decimal).replace("0x","")

"""Convert hex to decimal and binary to decimal"""
print("Decimal value of hex {} is".format(hexadecimal),int(hexadecimal,16))
print("Decimal value of binary {} is".format(binary),int(binary,2))  
"""Convert hexadecimal to binary and viceversa"""
print("Binary value of hex {} is".format(hexadecimal),bin(int(hexadecimal,16)).replace('0b',""))

print("Hex value of binary {} is".format(binary),hex(int(binary,2)).replace('0x',""))
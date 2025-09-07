"""
Valid or invalid ip

"""

text="10.1.1.1 256.265.255.255 255.255.25555.2555"

import re

response=re.compile(r'[0-2][0-5]{0,2}\.[0-2][0-5]{0,2}\.[0-2][0-5]{0,2}\.[0-2][0-5]{0,2}')

match=response.finditer(text)

for i in match:
    print(i)
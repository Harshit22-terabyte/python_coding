"""
Task
You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of  that contains  or more vowels.
Also, these substrings must lie in between  consonants and should contain vowels only.

Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format

A single line of input containing string .

Constraints


Output Format

Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.

Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output

ee
Ioo
Oeo
eeeee
Explanation

ee is located between consonant  and .
Ioo is located between consonant  and .
Oeo is located between consonant  and .
eeeee is located between consonant  and .
"""


import re

txt = "abaabaabaabaae"

# Correct regex using lookbehind and lookahead
pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

# Find meaningful matches
vowel_groups = re.findall(pattern, txt)

# Output results
if len(vowel_groups) == 0:
    print("-1")
else:
    for group in vowel_groups:
        print(group)

""" IMP concept of lookahead and lookbehind (?=,?<=)""" 

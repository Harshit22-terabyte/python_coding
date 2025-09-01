"""

Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

NOTE - If there are no repeating characters return '#'.

Example 1:

Input:
S = "geeksforgeeks"
Output: g
Explanation: g, e, k and s are the repeating
characters. Out of these, g occurs first.
Example 2:

Input:
S = "abcde"
Output: -1
Explanation: No repeating character present. (You need to return '#')

"""


# User function Template for python3

class Solution:
    def firstRep(self, s):
        # code here
        dict_count = dict()
        for i in s:
            if i not in dict_count.keys():
                # print("Added {}".format(i))
                dict_count[i] = 1
            else:
                # print("Incremented {}".format(i))
                dict_count[i] = dict_count[i] + 1

        for i, j in dict_count.items():
            if j > 1:
                print(i)
                exit()

a=Solution()
a.firstRep("geeksforgeeks")

"""
Given a string s of lowercase alphabets, You have to check that  it is isogram or not.
An Isogram is a string in which no letter occurs more than once.

Examples:

Input: s = "machine"
Output: true
Explanation: "machine" is an isogram as no letter has appeared twice. so we return true.
Input: s = "geeks"
Output: false
Explanation: "geeks" is not an isogram as 'e' appears twice. so we return false.
Constraints:
1 ≤ |s| ≤ 103
"""

class Solution:
    def isIsogram(self,s):
        dict_count = dict()
        for i in s:
            if i not in dict_count.keys():
                dict_count[i] = 1
            else:
                dict_count[i] += 1
                return False
        return True

a=Solution()
print(a.isIsogram("geeks"))
print(a.isIsogram("machine"))
"""
Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.

Examples:

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat.
Input: s = "racecar"
Output: 'e'
Explanation: In the given string, 'e' is the only character in the string which does not repeat.
Input: s = "aabbccc"
Output: '$'
Explanation: All the characters in the given string are repeating.
Constraints:
1 ≤ s.size() ≤ 105


"""

class Solution:
    def nonRepeatingChar(self,s):
        #code here
        dict_count = dict()
        for i in s:
            if i not in dict_count.keys():
                # print("Added {}".format(i))
                dict_count[i] = 1
            else:
                # print("Incremented {}".format(i))
                dict_count[i] = dict_count[i] + 1

        for i, j in dict_count.items():
            if j == 1:
                return i
                pass

        return '$'
a=Solution()
b=a.nonRepeatingChar("geeksforgeeks")
print(b)
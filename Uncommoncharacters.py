"""
You are given two strings s1 and s2. Your task is to identify the characters that appear in either string but not in both (i.e., characters that are unique to one of the strings). Return the result as a sorted string.
Examples:

Input: s1 = "geeksforgeeks", s2 = "geeksquiz"
Output: "fioqruz"
Explanation: The characters 'f', 'i', 'o', 'q', 'r', 'u', and 'z' are present in either s1 or s2, but not in both.
Input: s1 = "characters", s2 = "alphabets"
Output: "bclpr"
Explanation: The characters 'b', 'c', 'l', 'p', and 'r' are present in either s1 or s2, but not in both.
Input: s1 = "rome", s2 = "more"
Output: ""
Explanation: Both strings contain the same characters, so there are no unique characters. The output is an empty string.
Constraints:
1<= s1.size(), s2.size() <= 105
Both strings contain only lowercase English letters.
"""

#User function Template for python3

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
        uncommon_chars = list()
        for i in s1:
            if i not in s2:
                if i not in uncommon_chars:
                    uncommon_chars.append(i)
        for j in s2:
            if j not in s1:
                if j not in uncommon_chars:
                    uncommon_chars.append(j)
        uncommon_chars.sort()
        uncommon_string = "".join(uncommon_chars)
        return uncommon_string


a = Solution()
b=a.uncommonChars("swknwhkhhr", "cgx")
print(b)


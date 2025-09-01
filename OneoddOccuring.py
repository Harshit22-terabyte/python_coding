"""
Given an array of arr[] positive integers where all numbers occur even number of times except one number which occurs odd number of times. Return that number.

Examples:

Input:arr[] = [1, 2, 3, 2, 3, 1, 3]
Output: 3
Explaination: 3 occurs three times.
Input:arr[] = [5, 7, 2, 7, 5, 2, 5]
Output: 5
Explaination: 5 occurs three times.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106
"""
class Solution:
    def getOddOccurrence(self, arr):
        dict_count = dict()
        for i in arr:
            if i not in dict_count.keys():
                # print("Added {}".format(i))
                dict_count[i] = 1
            else:
                # print("Incremented {}".format(i))
                dict_count[i] = dict_count[i] + 1

        for i,j in dict_count.items():
            if j % 2 != 0:
                return i


a=Solution()
b=a.getOddOccurrence(arr=[1,2,3,2,3,1,3])
print(b)
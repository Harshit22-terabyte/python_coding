"""
Given an array of elements occurring in multiples of k, except one element which doesn't occur in multiple of k. Return the unique element.

Examples:

Input: k = 3, arr[] = [6, 2, 5, 2, 2, 6, 6]
Output: 5
Explanation: Every element appears 3 times except 5.
Input: k = 4, arr[] = [2, 2, 2, 10, 2]
Output: 10
Explanation: Every element appears 4 times except 10.

"""

class Solution:
    def find_unique(self, k, arr):
        #code here
        dict_count = dict()
        for i in arr:
            if i not in dict_count.keys():
                # print("Added {}".format(i))
                dict_count[i] = 1
            else:
                # print("Incremented {}".format(i))
                dict_count[i] = dict_count[i] + 1

        for i, j in dict_count.items():
            if j !=k:
                print(i)


a=Solution()
b=Solution()
a.find_unique(3,[6,2,5,2,2,6,6])
b.find_unique(4,[2,2,2,10,2])

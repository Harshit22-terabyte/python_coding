"""Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".

A tuple is a collection of items that are ordered and unchangeable.

Examples:

Input:
arr = (1, 2, 3, 4, 5, 4)
Output: False
Input:
arr = (1, 2, 3, 4, 5)
Output: True
"""


#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"

########### Write your code above ###############
def distinct_tuple(arr):
    set_arr=set(arr)
    if (len(set_arr)==len(arr)):
        print("True")
        
    else:
        print("False")
    
    

distinct_tuple(arr)
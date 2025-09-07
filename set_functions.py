"""

This is the last practice question of Python Set. You are familiar with working on the set in Python. Now, let's move on to work on two sets using some inbuilt functions which are used widely. They are:
union(): Used to find union() between two sets. It performs this using '|' operator.
intersection(): Used to find intersection() between two sets. It performs this using '&' operator.
difference(): Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly for B - A holds the same.

Now, Given some elements in two sets a and b, the task is to find the elements common in two sets, elements in both the sets, elements that are only in set a, not in b.
"""

# Function to find common elements in sets
# should return the intersection of sets
def common_in_set(a, b):
    # Your code here
    return a & b
    

# Function to find difference in sets
# Should return the difference in sets
def diff(a, b):
    # Your code here
    return a - b



# Function to find union of sets
# Should return the union of sets
def all_in_set(a, b):
    # Your code here
    
    return a | b
    
    
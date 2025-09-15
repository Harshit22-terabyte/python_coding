#!/bin/python

import math
import os
import random
import re
import sys


Sample input 
aWESOME is cODING
Output
Coding IS Awesome
#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#
def reverse_words_order_and_swap_cases(sentence):
    sentence_list=sentence.strip().split()
    sentence_list.reverse()
    new_list=[]
    for i in sentence_list:
        new_list.append(i.swapcase())
    string_output=" ".join(new_list)
    return string_output
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = raw_input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()

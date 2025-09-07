# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
"""
Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

"""


def words_length(words,chars):
    dict_chars_freq={}
    for i in chars:
        if i not in dict_chars_freq.keys():
            dict_chars_freq['{}'.format(i)]=0
        else:
            dict_chars_freq['{}'.format(i)]=dict_chars_freq['{}'.format(i)]+1
    sum=0
    for i in words:
        count=0
        for j in i:
            if j in dict_chars_freq.keys():
                count=count+1
            if (count==len(i)):
                sum=sum+count
    
    print(sum)
                
            
            
                
                
               
words_length(words = ["cat","bt","hat","tree"],chars = "atach" )
words_length(words = ["hello","world","leetcode"], chars = "welldonehoneyr")
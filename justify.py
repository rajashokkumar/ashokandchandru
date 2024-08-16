# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:39:17 2024

@author: asrajend

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

"""

words =  ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

def findcurrlen(curr):
    out = " ".join(curr)
    return len(out)

def getadjusted(curr, k):
    baselen = len("".join(curr))
    nospaces = k - baselen  
    # print(f"number of spaces to add {nospaces} baselen={baselen} k={k} curr_len={len(curr)}")
            
    while nospaces > 0:
        # print(f"value if no of space is = {nospaces}")
        for n in range(len(curr)-1):
            curr[n] = curr[n]+ " "
            # print(f"added space to {curr[n]} alue of n = {n}")
            nospaces -=1
            if nospaces <= 0:
                break
    out = "".join(curr)
    return out
    
    
def justify(words, k):
    output = []
    curr = []
    
    for word in words:
        if findcurrlen(curr) + len(word)+1 > k:
            out = getadjusted(curr, k)
            # print(len(out)) 
            # print(out)
            output.append([out])
            curr = []
            curr.append(word)
        else:
            curr.append(word)

    if findcurrlen(curr) > 0:
        out = getadjusted(curr, k)
        # print(len(out)) 
        # print(out)
        output.append([out])
    
    # print(output)
    for item in output:
        print(item)
    
    # print(out)

justify(words, k)

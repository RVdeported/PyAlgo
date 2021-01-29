# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:56:16 2021

@author: Roman
"""

import hashlib as hl

def sub_count(s: str) -> int:
    assert len(s) > 0, 'No empty strings'
    
    len_s = len(s)
    #s_hash = hl.sha1(s.encode('utf-8')).hexdigest()
    letters = str([chr(i) for i in range(ord('A'), ord('z') + 1)] + [' '])
    count = [0]

    for n in range(len_s):
        test_sub = ""
        for t in range(1, len_s + 1):
            if (n + t > len_s):
                break
            for i in range(t):
                for l in letters:
                    test_sub += l
                    if (hl.sha1(s[n : n + i + 1].encode('utf-8')).hexdigest() ==
                        hl.sha1(test_sub.encode('utf-8')).hexdigest()):
                        if (i == t - 1):
                            count[0] += 1
                        break
                    else: test_sub = test_sub[:-1]
    return count[0]

def Fib(n: int)-> int:
    fib = 0
    for t in range(n + 1):
        fib += t
    return fib
        

inp = input("Enter Latin string: \n")
count = sub_count(inp)
print(f'Count substrings: {count} and is correct: {Fib(len(inp))==count}')
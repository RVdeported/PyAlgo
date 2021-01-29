# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:31:28 2021

@author: Roman
"""

def HaffEncode(s: str):
    assert len(s) > 0, 'No empty strings' 
    uniq = [None,None, None]
    uniq[0] = list(set(s))                   # uniq chars
    uniq[1] = [s.count(i) for i in uniq[0]]  # counts
    uniq[2] = [""] * len(uniq[0])            # code for chars

    # sorting...
    for n in range(len(uniq[0])):
        changed = False
        for t in range(len(uniq[0]) - 1):
            if (uniq[1][t] > uniq[1][t + 1]):
                changed = True
                uniq[0][t], uniq[0][t+1], uniq[1][t], uniq[1][t+1] = uniq[0][t+1], uniq[0][t], uniq[1][t+1], uniq[1][t]
        if (not changed):
            break
    
    items = [[i] for i in uniq[0]]  # the future tree
    
    def getval(val): # get count of char if val is char
        if type(val) == str:
            val = uniq[1][uniq[0].index(val)]
        return val
    while len(items) > 1:
        vals = [getval(items[0][0]), getval(items[1][0])]
        items[0] = [vals[0] + vals[1], items[0], items[1]]
        items.remove(items[1])
        items.sort(key = lambda t:getval(t[0]))
    
    def encode_branch(branch, ansestors):
        if type(branch[0]) == str:
            uniq[2][uniq[0].index(branch[0])] = ansestors
            return
        encode_branch(branch[1], ansestors + '0')
        encode_branch(branch[2], ansestors + '1')
        
    encode_branch(items[0],"")
    res = ""
    for n in s:
        res += uniq[2][uniq[0].index(n)] + " "
    return res, items
    
res, tree = HaffEncode(input("Please, enter string for test"))
print("Result is: "+ res)
print("Tree is presented below:\n" + str(tree))


# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:15:41 2021

@author: Roman
"""

"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям 
(по одному разу). Сколько рукопожатий было?
"""


def handshakes(N):
    count = 0
    connections = [0] * (N * N) # 1D empty graph
    for i in range(N):
        for t in range(N):
            if (i != t): # excluding self-shackes
                if (connections[i * N + t] == 0 and # calculations of i -> t and t -> i connections coords
                    connections[t * N + i] == 0):
                    count += 1
                    connections[i * N + t] = 1
                    connections[t * N + i] = 1
    return count
    
inp = int(input("Please, enter num (no cheasey letters pls): "))
count = handshakes(inp)
print(f'Total count is: {count}')
                
               
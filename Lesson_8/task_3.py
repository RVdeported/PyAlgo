# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:28:21 2021

@author: Roman
"""

graph = [
        [0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]
        ]


def depth_search(target, start, visited = []):
    visited.append(start)
    if (target == start):
        print(f'Here is {target}!')
        return True
    for i, n in enumerate(graph):
        if (graph[start][i] > 0 and
            visited.count(i) == 0):
            print(f'Visiting {i} from {start}...')
            if (depth_search(target, i, visited)):
                return True
    return False
            
depth_search(3, 0)
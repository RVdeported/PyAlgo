# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:49:35 2021

@author: Roman
"""

graph = [
        [0, 9, 1, 8, 1],
        [9, 0, 0, 0, 0],
        [0, 0, 0, 2, 0],
        [8, 0, 0, 0, 1],
        [0, 0, 0, 1, 0]
        ]

def path(fr):
    
    costs = [999] * len(graph) # kind of infinit
    curr_cost = 0
    costs[fr] = 0 
    path = []
    # creating matrix of paths by value
    for i in range(len(graph)):
        path.append([])
    getCosts(fr, costs, curr_cost, path)
    return costs, path

def getCosts (fr, costs, curr_cost, path):
    path[fr].append(fr)
    for i in range(len(graph)):
        if (graph[fr][i] > 0 and 
            costs[i] > curr_cost + graph[fr][i]
            ):
            path[i] = list(path[fr]) # pasting new path by value
            costs[i] = curr_cost + graph[fr][i]
            curr_cost += graph[fr][i]
            getCosts(i, costs, curr_cost, path)
            curr_cost -= graph[fr][i] # refreshing costs for the next node
            
costs, path = path(0)
print(f'Mininimal costs to each node is as follows: {costs}')
print(f'Shortest route are as follows (numbers represent node num):')
for i in range(len(path)):
    print(f'{i}: {path[i]}')
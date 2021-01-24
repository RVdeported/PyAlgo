# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:52:02 2021

@author: Roman
"""

"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого — цифры числа.
"""

from collections import deque

nums = ['0', '1', '2', '3', '4', 
        '5', '6', '7', '8', '9', 
        'A', 'B', 'C', 'D', 'E', 'F']

def FromIntToListHex(num):
    summ_arr = []
    while (num > 0):
        summ_arr.append(nums[num % 16])
        num //= 16
    summ_arr.reverse()
    return summ_arr

inp = input("Please, enter the nums via space: ").split(" ")
num_1 = deque(inp[0])
num_2 = deque(inp[1])
summ = 0
args = [0, 0]
for ind, t in enumerate([num_1, num_2]):
    for i, n in enumerate(t):
        # algo starts from other end of array, so (len(t) - i -1) instead of just i. Kinda lazy now do the pop() thing
        args[ind] += nums.index(n) * (16 ** (len(t) - i - 1)) 

summ_arr = FromIntToListHex(sum(args))
mult_arr = FromIntToListHex(args[0] * args[1])

print(f'Sum of numbers is: {summ_arr}')
print(f'Multiplication product of numbers is: {mult_arr}')
    






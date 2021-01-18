# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:36:27 2021

@author: Roman
"""

"""
5. В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию в массиве.
"""
import random as r
nums = [r.randint(-99,99) for n in range(10)]

cur_max = 0
# initialization
while (nums[cur_max] > 0 and cur_max < len(nums)): 
    cur_max += 1
# solving
for i, n in enumerate(nums):
    if (n < 0 and n > nums[cur_max]):
        cur_max = i

print("Array of random elements:\n")
print(nums)
print(f'Index of highes negative number is {cur_max} with value {nums[cur_max]}')
        
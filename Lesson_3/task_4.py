# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:28:05 2021

@author: Roman
"""
"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random as r

nums = [r.randint(0,5) for n in range(10)]
count = [0] * len(nums)
for i, n in enumerate(nums):
    for n2 in nums:
        if (n == n2):
            count[i] += 1
cur_max = 0
for i, n in enumerate(count):
    if (n > count[cur_max]):
        cur_max = i
        
print("Random Array:\n")
print(nums)
print(f'Must often num is: {nums[cur_max]}')

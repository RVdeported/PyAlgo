# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:18:46 2021

@author: Roman
"""

"""
2. Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
второй массив надо заполнить значениями 0, 3, 4, 5 
(помните, что индексация начинается с нуля), т. к. именно в этих 
позициях первого массива стоят четные числа.
"""
import random as r

nums = [r.randint(0,99) for n in range(10)]
out = []
for i, n in enumerate(nums):
    if (n % 2 == 0):
        out.append(i)

print("Array of random elements:\n")
print(nums)
print("Indexes with even nums:\n")
print(out)
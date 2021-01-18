# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:11:29 2021

@author: Roman
"""

import random
import string

"""
2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
 проходящей через эти точки.

print("2. По введенным пользователем координатам двух точек...\n")
"""

inp = input("Enter data via space in order: y1 x1 y2 x2.\n").split(" ")
y1 = int(inp[0])
x1 = int(inp[1])
y2 = int(inp[2])
x2 = int(inp[3])

if (x1 == x2):  k = 0
else: k = (y1 - y2) / (x1 - x2)
    
b = y1 - k * x1

check1 = k * x1 + b
check2 = k * x2 + b

if (k != 0):
    print("Function params are: k = " + str(round(k,2)) + " b = " + str(round(b,2)))
    print("check 1: k * x1 + b = y1? : "+ str(int(check1) == y1))
    print("check 2: k * x2 + b = y2? : "+ str(int(check2) == y2))
else:
    print("Function params are: k = " + str(round(k,2)) + " b1 = " + str(y1) + " b2 = " + str(y2))

"""
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
"""

print("\n3. Написать программу, которая генерирует в указанных пользователем границах...\n")

def isfloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
        


inp = input("Enter borders of desired format via space:\n").split(" ")

if (inp[0].isdigit() and inp[1].isdigit()):
    inp[0] = int(inp[0])
    inp[1] = int(inp[1])
    out = random.randint(min(inp[0], inp[1]), max(inp[0], inp[1]))
elif (isfloat(inp[0]) and isfloat(inp[1])):
    inp[0] = float(inp[0])
    inp[1] = float(inp[1])
    rand_int = random.randint(min(int(inp[0]), int(inp[1])), 
                              max(int(inp[0]), int(inp[1])))
    rand_dec = random.randint(0,99)
    out = float(rand_int) + (float(rand_dec) / 100)
elif (not(inp[0].isnumeric()) and not(inp[1].isdecimal())):
    letters = string.ascii_letters
    index1 = letters.index(inp[0])
    index2 = letters.index(inp[1])
    rand = random.randint(min(index1, index2),max(index1, index2))
    out = letters[rand]
else:
    print("Wrong input")
    out = False
print("Result is: " + str(out))


"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, 
и сколько между ними находится букв.
"""

print("\n4. Пользователь вводит две буквы. Определить, на каких местах алфавита...\n")

inp = input("Enter letters via space:\n").split(" ")
Letters = string.ascii_letters
inp[0] = inp[0].lower()
inp[1] = inp[1].lower()
ind_1 = Letters.index(inp[0]) + 1
ind_2 = Letters.index(inp[1]) + 1
dist = abs(ind_1 - ind_2)

print("Result is: first index: "+str(ind_1) + " second index: "+str(ind_2)+" distance: "+str(dist))

"""
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
print("\n5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.\n")
inp = int(input("Enter alphabet index (English only)\n"))
Letters = string.ascii_letters
out = Letters[inp - 1]
print("Result is: " + out)




# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:40:22 2021

@author: Roman
"""

"""
1. Написать программу, которая будет складывать, вычитать, 
умножать или делить два числа. Числа и знак операции вводятся пользователем. 
После выполнения вычисления программа не завершается, а запрашивает новые 
данные для вычислений. Завершение программы должно выполняться при вводе 
символа '0' в качестве знака операции. Если пользователь вводит неверный 
знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и 
снова запрашивать знак операции. Также она должна сообщать пользователю о 
невозможности деления на ноль, если он ввел его в качестве делителя.
"""
print("1. Написать программу, которая будет складывать, вычитать...")
while (True):
    inp = input("Enter a num, arithmetic sign and another num via space:\n").split(" ")
    inp[0] = float(inp[0])
    inp[2] = float(inp[2])
    while (inp[1] != '+' and inp[1] != '-' and
           inp[1] != '*' and inp[1] != '/' and 
           inp[1] != '0'):
        inp[1] = input(f"Expected '0', '+', '-', '*' or '/' but got {inp[1]} as second paramter. Please, enter another value:\n")
    if (inp[1] == '0'):
        print("Exiting the program.")
        break
    if (inp[1] == '/' and inp[2] == '0'):
        print("Error! You can't divide by zero")
        continue
    res = 0
    if (inp[1] == '+'):
        res = inp[0] + inp[2]
    elif (inp[1] == '-'):
        res = inp[0] - inp[2]
    elif (inp[1] == '*'):
        res = inp[0] * inp[2]
    else:
        res = inp[0] / inp[2]
    print(f'Result of operation {inp[0]} {inp[1]} {inp[2]} is {res}')


"""
2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и
2 нечетные (3 и 5).
"""
print("\n2. Посчитать четные и нечетные цифры введенного натурального числа.\n")

def RecOdd (a, count = 0):
    if (a % 2 == 1):
        count += 1
    if (a < 10):
        return count
    return RecOdd(a // 10, count)

inp = int(input("Enter a num to test odd function: "))
print(f'In num {inp} there is {RecOdd(inp)} odd number(s)')

"""
3. Сформировать из введенного числа обратное по порядку входящих 
в него цифр и вывести на экран. Например, если введено число 3486, 
надо вывести 6843.
"""
print("\n 3. Сформировать из введенного числа обратное по порядку входящих...\n")
 
inp = int(input("Enter a num for reverse num demonstration: "))
 
while ( inp != 0):
     print(inp % 10, end = '')
     inp //=10

"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 
Количество элементов (n) вводится с клавиатуры.
"""

inp = int(input("Please, enter num of iterations for negative double-down sum: "))
n = inp
num = 1
res = 0
while(inp != 0):
    print(f'Adding {num}...')
    res += num
    num = -num / 2
    inp -= 1

print(f'Total result is: {res}')






    
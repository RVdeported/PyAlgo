# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:23:17 2021

@author: Roman
"""

"""
1. Пользователь вводит данные о количестве предприятий, их 
наименования и прибыль за четыре квартала для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех 
предприятий) и отдельно вывести наименования предприятий, 
чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

company = namedtuple('comp',["name","income"])
companies = []

while(True):
    inp = input("Please, enter name and income of a company via space to add it or press '-1' to exit: ").split(" ")
    if (inp [0] == "-1"):
        break
    companies.append(company(inp[0],int(inp[1])))

average_inc = sum([i.income for i in companies]) / len(companies)
above_avg = [i.income > average_inc for i in companies]
higher_comp = [i.name for ind, i in enumerate(companies) if above_avg[ind]]
lower_comp =  [i.name for ind, i in enumerate(companies) if not above_avg[ind]]
print(f'Average income is {average_inc}.')
print(f'Companies above avg are: {higher_comp}')
print(f'Companies below avg are: {lower_comp}')



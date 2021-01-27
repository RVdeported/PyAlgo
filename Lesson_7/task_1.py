# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:55:40 2021

@author: Roman
"""
"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный 
случайными числами на промежутке [-100; 100). Выведите на экран исходный и 
отсортированный массивы.
"""

import random

def execute(size):
    arr = [random.randint(-100,100) for i in range(size)]
    bubble_upd(arr)

def bubble_upd(arr):
    leng = len(arr)
    n = 0
    while n < leng:
        for i in range(leng - n - 1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n += 1
    """
    magic block: here is acceleration by moving
    curr hugest item at the end of array
    """
        t = 0
        while t < leng - n - 2:
            if (arr[t] == arr[leng-n]):
                arr[t], arr[leng-n-1] = arr[leng-n-1],arr[t]
                n += 1
            t += 1

            
         
def bubble(arr):
    leng = len(arr)
    for n in range(leng):
        for i in range(leng - n - 1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
    

arr = [random.randint(-100,100) for i in range(100)]
true_arr = sorted(arr)
print(f'initial arr:\n{arr}')
bubble_upd(arr)
print(f'sorted arr:\n{arr}')
print(f'arr sorted correctly: {arr == true_arr}')

"""
timeit показывает небольшое преимущество улучшенной версии. Это преимущество выше с ростом
одинаковых элементов, но он замедляет процесс, если равных чисел мало.
"""

"""
bubble_upd
(base) C:\Users\Roman\Desktop\DataScience course\Python_Algo\Lesson_7>python -m timeit -n 1000 -s "import task_1" "task_1.execute(100)"
1000 loops, best of 3: 752 usec per loop

bubble:
(base) C:\Users\Roman\Desktop\DataScience course\Python_Algo\Lesson_7>python -m timeit -n 1000 -s "import task_1" "task_1.execute(100)"
1000 loops, best of 3: 982 usec per loop
"""
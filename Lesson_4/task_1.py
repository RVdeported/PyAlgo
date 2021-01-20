# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:45:29 2021

@author: Roman
"""

"""
1. В диапазоне натуральных чисел от 2 до 99 определить, 
сколько из них кратны каждому из чисел в диапазоне от 2 до 9. 
Примечание: 8 разных ответов.
"""

def original(n):
    res = [0] * 8
    for j in range(2, 10):
        for i in range(2, n+1):
            if i % j == 0:
                res[j-2] += 1
    return res

def useless_recursion(n, start = 2):
    if (start > 9):
        return []
    count = 0
    for i in range(2, n + 1):
        if (i % start == 0):
            count += 1
    res = [count]
    res += useless_recursion(n, start + 1)
    return res

def cheated(n):
    res = [0] * 100
    for t in range(2,102):
        res[t-2] = n // t
    return res


"""
Первые две функции выполняют работу почти с линейной сложностью, что очень неплохой результат.

На удивление рекурсивный алгоритм работает быстрее циклического, хотя
я ожидал, что это будет полностью бесполезная идея. Как и ожидалось,
Функция вызывает себя 9 раз на каждое число кратность к которому надо выявить
+ 1, которая просто говорит о завершении рекурсии, сводка есть ниже.

Ну и читовый алгоритм, как ожидалось, лидирует с почти константным временем.
Конечно, это изменится с увеличением простых чисел, сложность может вырости и до
n^2, где n - список простых чисел, но даже при 100 числах он работает 
быстрее циклического и рекурсивного.

Для первого и последнего алгоритма не включаю статистику cProfile так
как без рекурсии в этом нет особо смысла.
"""
    
"""
original stats:

python -m timeit -n 1000 -s "import task_1" "task_1.original(99)"
1000 loops, best of 3: 67.3 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.original(1000)"
1000 loops, best of 3: 765 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.original(4000)"
1000 loops, best of 3: 3.16 msec per loop
"""

"""
useless_recursion stats:

python -m timeit -n 1000 -s "import task_1" "task_1.useless_recursion(99)"
1000 loops, best of 3: 60.6 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.useless_recursion(1000)"
1000 loops, best of 3: 631 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.useless_recursion(4000)"
1000 loops, best of 3: 2.55 msec per loop

cProfile.run('useless_recursion(1000)')
         12 function calls (4 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      9/1    0.001    0.000    0.001    0.001 <ipython-input-40-c4e3bd16915d>:10(useless_recursion)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

"""
cheated stats:

Lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.cheated(99)"
1000 loops, best of 3: 0.925 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.cheated(1000)"
1000 loops, best of 3: 0.951 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.cheated(4000)"
1000 loops, best of 3: 1.05 usec per loop
"""








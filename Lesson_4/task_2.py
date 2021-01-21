# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:44:01 2021

@author: Roman
"""
import functools
import math

@functools.lru_cache(10000)
def create_table(size):
    arr = [0] * size
    for n in range(2,size):
        if (arr[n] == 0):       
            not_s = 2 * n
            while not_s < size:
                arr[not_s] = 1
                not_s += n
    return arr

def prime_num_er(num, table_size = 10000):
    arr = create_table(table_size)
    res = 0
    i = 2
    while(num > 0):
        for t in range(i, table_size):
            if (arr[t] == 0):
                res = t
                num -= 1
                i = t + 1
                break
            if (t == table_size - 1):
                table_size *= 2
                arr = create_table(table_size)
    return res

def prime_num_mod(num):
    res = 0
    to_test = 2
    while (num > 0):
        is_prime = True
        for n in range(2, int(math.sqrt(to_test)) + 1):
            if (to_test % n == 0):
                is_prime = False
                break
        if (is_prime):
            res = to_test
            num -= 1
        else:
            is_prime = True
        if (to_test > 2):
            to_test += 2
        else:
            to_test += 1
    return res

#print(prime_num_mod(1000))
"""
На первых порах выглядело так, что имеет смысл сделать таблицу Эратосфена и ориентироватся по ней.
Но после пары изменений во втором алгоритме 
(такие как проверка до корня тестируемого числа и тест только нечетных чисел),
оказалось, что это более эффективный способ. 
"""

"""
prime_num_er stats:
    
python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_er(10)"
1000 loops, best of 3: 6.26 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_er(100)"
1000 loops, best of 3: 95.7 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_er(200)"
1000 loops, best of 3: 201 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_er(300)"
1000 loops, best of 3: 342 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_er(400)"
1000 loops, best of 5: 575 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_er(500)"
1000 loops, best of 5: 742 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_er(1000)"
1000 loops, best of 5: 1.7 msec per loop
"""

"""
prime_num_mod stats:
    
python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_mod(10)"
1000 loops, best of 5: 6.02 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_mod(100)"
1000 loops, best of 5: 68.9 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_mod(200)"
1000 loops, best of 5: 134 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_mod(300)"
1000 loops, best of 5: 223 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_mod(400)"
1000 loops, best of 5: 317 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_mod(500)"
1000 loops, best of 5: 383 usec per loop

python -m timeit -n 1000 -s "import task_2" "task_2.prime_num_mod(1000)"
1000 loops, best of 5: 738 usec per loop
"""
        
# Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках практического задания первых трех уроков.

# Определить, какое число в массиве встречается чаще всего.

import random
from timeit import timeit
import cProfile


# SIZE = 100
# array = [random.randint(1, SIZE // 1.5) for _ in range(SIZE)]
# print(array)

def findElem1(size):
    array = [random.randint(1, size // 1.5) for _ in range(size)]
    unique_elems = list(set(array))
    max_appearances = 1
    result = unique_elems[0]

    for unique_num in unique_elems:
        appearances = 0
        for num in array:
            if num == unique_num:
                appearances += 1
        if appearances > max_appearances:
            result = unique_num
            max_appearances = appearances
    if max_appearances > 1:
        return result
    return False


def findElem2(size):
    array = [random.randint(1, size // 1.5) for _ in range(size)]
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        return num
    return False


def findElem3(size):
    array = [random.randint(1, size // 1.5) for _ in range(size)]
    frequency = 1
    num = array[0]
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    if frequency > 1:
        return num
    return False



# n = 100
# print(timeit('findElem1(100)', number=100, globals=globals())) # 0.02715789998183027
# print(timeit('findElem2(100)', number=100, globals=globals())) # 0.017132899985881522
# print(timeit('findElem3(100)', number=100, globals=globals())) # 0.03756589998374693


# n = 1000
# print(timeit('findElem1(1000)', number=100, globals=globals())) # 1.2670526999863796
# print(timeit('findElem2(1000)', number=100, globals=globals())) # 0.17256600002292544
# print(timeit('findElem3(1000)', number=100, globals=globals())) # 2.424129599996377

# cProfile.run('findElem1(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.014    0.014    0.019    0.019 les_4_task_1.py:15(findElem1)

# cProfile.run('findElem2(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 les_4_task_1.py:34(findElem2)

# cProfile.run('findElem3(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.024    0.024    0.028    0.028 les_4_task_1.py:53(findElem3)

# Вывод findElem2 - самый быстрый и эффективный ввиду того, что расчеты проводятся быстрее
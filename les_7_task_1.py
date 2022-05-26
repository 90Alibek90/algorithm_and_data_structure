# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.

import random

def bubble_sort(arr):
    n = 1

    while n < len(arr):
        count = 0

        for i in range(len(arr) - 1 - (n - 1)):

            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1

        if count == 0:
            break

        n += 1

SIZE = 15
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print('Массив: ', array, sep='\n')
bubble_sort(array)
print('После сортировки пузырьком: ', array, sep='\n')

# Определить, какое число в массиве встречается чаще всего.

import random

array = [random.randint(1, 20) for _ in range(30)]
unique_elems = list(set(array))
print(array)
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

print(result)
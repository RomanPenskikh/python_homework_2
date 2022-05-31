# Найти сумму чисел списка стоящих на нечетной позиции
# Пример [1,2,3,4] = 4
from array import array
from operator import truth


array = [1, 2, 3, 4, 5, 6, 7, 8]
len_pos = len(array)
sum_pos = 0
count = 0
for i in range(len_pos):
    if (array[i] %2) != 0:
        count += array[i]
print(count)

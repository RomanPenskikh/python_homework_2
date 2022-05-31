# В заданном списке вещественных чисел найдите разницу между минимальным и максимальным значением дробной части элемента
# [1.1, 1.2, 3.1, 5, 10.01] =>0.19
from array import array
import math


array = [1.1, 1.2, 3.1, 5, 10.01]
int_array=[]
def new_array(list):
    for i in range(0,5):
        if type(list[i])!=int:
            int_array.append(list[i])
    return int_array
print(new_array(array))
is_digit=0
def def_float(digit):
    min_d=math.modf(min(digit))
    max_d=math.modf(max(digit))
    is_digit=min_d[0]-max_d[0]
    return round(is_digit,2)
print(def_float(int_array))

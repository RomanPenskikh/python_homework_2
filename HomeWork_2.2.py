# Найти произведение пар чисел в списке . Парой читаем первый и последний элемент , второй и предпоследний и т.д.
# Пример: [2,3,4,5,6]=>[12,15,16]; [2,3,5,6] => [12,15]
from array import array


array=[2,3,4,5,6]
def a_array(a_list):
    kol_list = len(a_list)//2+len(a_list)%2
    b_list=[]
    for i in range (0, kol_list):
        b_list.append(a_list[i]*a_list[-(i+1)])
    return b_list
print(array)
print(a_array(array))

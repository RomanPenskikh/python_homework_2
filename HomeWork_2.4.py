#написать программу преобразования десятичного числа в двоичное
from itertools import count


def digit_ten(digit):
    memory=digit
    digit_two=1
    count = 0
    #digit_count=[]
    while memory > 0:
        #digit_count.append(digit_two-digit)
        count=count+memory%2*digit_two
        digit_two=digit_two*10
        memory=memory//2   
    print(count)
print('укажите десятичное число')
discover=int(input(''))
print(digit_ten(discover))



import math

num = int(input())

for i in range(num, 1, -1):  # проверяем от числа до 1
    if i == num:
        for j in range(2, num):  # проверяем от 2 до числа
            if math.pow(i, 1/j) % 1 == 0:  # если поделить число на степень и получится целое число, то выводим его
                print(int(i))
                exit()
    else:
        for j in range(2, int(math.sqrt(i))+1):  # проверяем от 2 до квадратного корня из числа
            if math.pow(i, 1/j) % 1 == 0:  # если поделить число на степень и получится целое число, то выводим его
                print(int(i))
                exit()

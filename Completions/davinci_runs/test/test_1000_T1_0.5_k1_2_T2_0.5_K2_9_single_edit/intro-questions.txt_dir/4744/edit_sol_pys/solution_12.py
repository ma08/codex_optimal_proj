

import math

# Вводим переменные
V = int(input("Введите объём параллелепипеда: "))
# Вычисляем все размеры параллелепипеда

a = math.ceil(V**(1/3))
b = math.ceil((V/a)**(1/2))
c = math.ceil(V/(a*b))

# Выводим площадь поверхности параллелепипеда
print("Площадь поверхности параллелепипеда равна: ", 2*(a*b + b*c + a*c))

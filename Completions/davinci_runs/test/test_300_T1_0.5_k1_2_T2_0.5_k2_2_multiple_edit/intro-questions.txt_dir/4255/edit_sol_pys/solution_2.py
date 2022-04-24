

import math
# Ввод данных и присваивание переменным

abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])
# Сравнение и вычисление

if a >= b and a >= c:
    if b >= c:
        p = (a + b + c) / 2
        print(p)
    else:
        p = (a + b + c) / 2
        print(p)
elif b >= a and b >= c:
    if a >= c:
        p = (a + b + c) / 2
        print(p)
    else:
        p = (a + b + c) / 2
        print(p)
else:
    if a >= b:
        p = (a + b + c) / 2
        print(p)
    else:
        p = (a + b + c) / 2
        print(p)

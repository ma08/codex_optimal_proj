"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
Программа должна быть эффективной и не выполнять лишних действий!
"""


a = [int(i) for i in input().split()]

divisors.sort()

x = 1
y = 1
for i in range(n):
    if i % 2 == 0:
        x *= divisors[i]
    else:
        y *= divisors[i]

print(x, y)

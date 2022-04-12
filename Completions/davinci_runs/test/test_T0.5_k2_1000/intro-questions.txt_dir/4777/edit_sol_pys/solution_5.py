# Программа выводит первые два числа Фибоначчи
k = int(input())

a = 0
b = 1

for _ in range(k):
    a, b = b, a+b

print(a, b)

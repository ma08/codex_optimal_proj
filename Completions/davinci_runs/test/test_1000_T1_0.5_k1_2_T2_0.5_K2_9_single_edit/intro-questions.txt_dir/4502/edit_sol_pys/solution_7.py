
import sys

n = int(input())
a = [int(s) for s in input().split()]  # список из введенных чисел

b = []
for i in range(n):  # добавление чисел в конец списка и переворот
    b.append(a[i])
    b.reverse()

print(*b)



n = int(input())  # количество чисел
a = [int(i) for i in input().split()]  # список чисел

max_rest = 0  # максимальное количество единиц подряд
rest = 0  # количество единиц подряд

for i in range(n):
    if a[i] == 1:  # если единица
        rest += 1
    else:  # если не единица
        max_rest = max(max_rest, rest)
        rest = 0

max_rest = max(max_rest, rest)  # если последнее число было единица

print(max_rest)

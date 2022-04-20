# Напишите программу, которая получает на вход два массива чисел, размером не более 10⁵, и выводит их пересечение. Числа в массивах различны и отсортированы по возрастанию.

n = int(input())
a = [int(x) for x in input().split()]

b = []

for i in range(n):
    if a[i] in a[n:]:
        b.append(a[i])
    else:
        for j in range(n, 2 * n):
            if a[j] == a[i]:
                b.append(a[j])
                break

print(*b)

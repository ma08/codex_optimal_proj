
n = int(input())
a = list(map(int, input().split()))
a.append(a[0]) # добавляем первый элемент в конец
a.append(a[1]) # добавляем второй элемент в конец

best = 0
length = 0

for i in range(n + 2): # рассматриваем все элементы в массиве, включая добавленные
    if a[i] == 1:
        length += 1
    else:
        best = max(best, length)
        length = 0

print(best)

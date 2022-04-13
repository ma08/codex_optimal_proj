

n = int(input())  # the number of numbers
a = list(map(int, input().split()))  # input numbers

g = [0] * n  # array for output
g[0] = a[0]  # first element of the array

for i in range(1, n):  # цикл для всех элементов
    if a[i] > g[-1]:  # если элемент больше последнего в массиве
        g.append(a[i])  # добавляем его
    else:
        for j in range(len(g)):  # для всех элементов в массиве
            if a[i] <= g[j]:  # если элемент меньше чем элемент массива
                g[j] = a[i]  # меняем его на этот
                break

print(len(g))  # вывод длины массива
print(*g)  # вывод массива

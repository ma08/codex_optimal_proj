
n = int(input())
a = list(map(int, input().split()))

q = [a[0]]  # создаем список и добавляем первый элемент из входного списка
for i in range(1, n):
    if a[i] <= 2 * q[-1]:  # если элемент из входного списка меньше или равен двукратному последнему элементу списка q
        q[-1] = a[i]  # перезаписываем последний элемент списка q
    else:
        q.append(a[i])  # иначе добавляем элемент в список q

print(len(q))

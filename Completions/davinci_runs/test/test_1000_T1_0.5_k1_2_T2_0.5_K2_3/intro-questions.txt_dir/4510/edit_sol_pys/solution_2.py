from collections import deque

n, k = map(int, input().split())  # число чисел, длина очереди
ids = list(map(int, input().split()))  # введенные числа

d = deque()  # очередь

for id in ids:  # проходим по введенным числам
    if id in d:  # проверяем есть ли число в очереди
        continue  # если есть пропускаем его
    if len(d) == k:  # если длина очереди равна длине очереди
        d.pop()  # удаляем последний элемент из очереди
    d.appendleft(id)  # добавляем элемент в начало очереди

print(len(d))  # выводим длину очереди
print(*d)  # выводим очередь

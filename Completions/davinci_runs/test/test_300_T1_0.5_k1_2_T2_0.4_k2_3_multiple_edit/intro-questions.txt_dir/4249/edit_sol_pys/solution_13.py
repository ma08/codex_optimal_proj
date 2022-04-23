
n, m = map(int, input().split())  # количество чашек и количество страниц
a = list(map(int, input().split()))  # количество страниц в каждой чашке

a.sort()  # сортируем массив чашек по возрастанию

cups = 0  # счетчик количества чашек
pages = 0  # счетчик количества страниц
days = 0  # счетчик количества дней

while cups < n:
    pages += a[cups]
    days += 1
    cups += 1
    if pages >= m:
        break  # если количество страниц больше или равно количеству страниц которые нужно прочитать
    if cups < n:
        pages -= days - 1

if pages < m:
    days = -1

print(days)

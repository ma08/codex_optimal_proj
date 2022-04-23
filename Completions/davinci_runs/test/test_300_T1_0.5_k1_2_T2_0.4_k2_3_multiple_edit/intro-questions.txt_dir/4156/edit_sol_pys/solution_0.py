
n, w = map(int, input().split())
a = list(map(int, input().split()))

i = -1
j = 0

while i < n:
    i += 1
    if a[i] > w or a[i] < -w:  # Если введенное число больше веса или меньше отрицательного веса
        print(0)
        break
    j += a[i]
    if j > w or j < 0:  # Если сумма чисел больше веса или меньше 0
        print(0)
        break

if i == n:  # Если не выполняется вышеперечисленные условия
    print(w-j+1)  # Печатаем количество вариантов

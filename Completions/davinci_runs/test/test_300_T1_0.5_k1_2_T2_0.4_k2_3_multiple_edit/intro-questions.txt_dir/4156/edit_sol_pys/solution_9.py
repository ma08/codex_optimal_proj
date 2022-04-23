
n, w = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 0

for i in range(n):
    if a[i] > w or a[i] < -w:  # Если введенное число больше веса или меньше отрицательного веса
        print(0)
        break
    j += a[i]
    if j > w or j < 0:  # Если сумма чисел больше веса или меньше нуля
        print(0)
        break

if i == n-1:  # Если не выполняется вышеперечисленные условия
    print(w-j+1)  # Печатаем количество вариантов

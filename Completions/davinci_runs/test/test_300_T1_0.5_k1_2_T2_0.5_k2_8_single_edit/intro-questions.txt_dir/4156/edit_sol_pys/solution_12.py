

n, w = map(int, input().split()) # количество пар и максимальная весовая сумма
a = list(map(int, input().split())) # пары коробок

i = 0 # индекс пары
j = 0 # весовая сумма

for i in range(n): # проверка на количество пар и весовую сумму
    if a[i] > w or a[i] < -w: # если вес коробки больше максимальной весовой суммы
        print(0)
        break
    j += a[i] # весовая сумма пар
    if j > w or j < 0: # если весовая сумма пар больше максимальной весовой суммы
        print(0)
        break

if i == n-1: # если проверка прошла
    print(w-j+1) # ответ

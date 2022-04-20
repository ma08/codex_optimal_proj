

N = int(input())  # количество чисел
a = [int(x) for x in input().split()]  # список чисел

count = 0  # количество проходов

for i in a:  # проходимся по списку
    while i % 2 == 0:  # пока число четное
        i /= 2  # делим его на 2
        count += 1  # добавляем проход

print(count)

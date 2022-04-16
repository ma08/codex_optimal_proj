

n = int(input())  # число вершин
a = list(map(int, input().split()))  # список смежности

disturbed = []  # список смежных вершин в которых нет построения

for i in range(1, n - 1):  # проверяем каждую вершину
    if a[i - 1] == a[i + 1] == 1 and a[i] == 0:  # если обе смежные вершины имеют постройки и исследуемая нет
        disturbed.append(i)  # добавляем вершину в список

print(len(disturbed))

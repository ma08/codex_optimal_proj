# file

pieces = [1, 1, 2, 2, 2, 8] # заданные количества фигур
count = [int(i) for i in input().split()] # введенные количества фигур

for i in range(6):
    print(pieces[i] - count[i], end=" ") # вывод недостающих фигур

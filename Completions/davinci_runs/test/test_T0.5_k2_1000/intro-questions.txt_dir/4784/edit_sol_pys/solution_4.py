
x = int(input()) # количество денег в кошельке
n = int(input()) # количество покупок

res = x
for i in range(n):
    res -= int(input()) # вычитаем каждую покупку

print(res)

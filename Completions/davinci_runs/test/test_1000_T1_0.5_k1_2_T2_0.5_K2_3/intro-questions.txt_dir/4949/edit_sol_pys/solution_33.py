

N, W, H = map(int, input().split())  # ввод переменных
for i in range(N):  # проверка на вхождение в квадрат
    if int(input()) <= max(W, H):  # проверка на вхождение в квадрат
        print("DA")
    else:
        print("NE")

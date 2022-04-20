# Проверка, является ли число составным

N = int(input())
if N > 1:
    for i in range(2, N):
        if N % i == 0:
            print("Yes")
            break
    else:
        print("No")
else:
    print("No")

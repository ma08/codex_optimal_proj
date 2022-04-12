
N = int(input())

if N < 1 or N > 180:  # проверка на выход за пределы
    print("impossible")
else:
    for i in range(20, 0, -1):  # проверка на возможность выполнения тройного броска
        if N >= i*3:
            print("triple", i)
            N -= i*3
            break
    for i in range(20, 0, -1):  # проверка на возможность выполнения двойного броска
        if N >= i*2:
            print("double", i)
            N -= i*2
            break
    for i in range(20, 0, -1):
        if N >= i:
            print("single", i)
            N -= i
            break
    if N != 0:
        print("impossible")

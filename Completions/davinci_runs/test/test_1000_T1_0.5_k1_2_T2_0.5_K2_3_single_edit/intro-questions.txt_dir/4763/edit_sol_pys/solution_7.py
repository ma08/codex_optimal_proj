
N = int(input())

if N < 1 or N > 180 or (N % 3 != 0 and N % 2 != 0):
    print("impossible")
else:
    for i in range(60, 0, -1):
        if N >= i*3:
            print("triple", i, end=' ')
            N -= i*3
            break
    for i in range(60, 0, -1):
        if N >= i*2:
            print("double", i, end=' ')
            N -= i*2
            break
    for i in range(60, 0, -1):
        if N >= i:
            print("single", i, end=' ')
            N -= i
            break
    if N != 0:
        print("impossible")

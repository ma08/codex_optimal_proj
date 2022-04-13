

N = int(input())

if N < 1 or N > 180:
    print("impossible")
else:
    for i in range(20, -1, -1):
        if N >= i * 3:
            print("triple", i)
            N -= i * 3
            break
    for i in range(20, -1, -1):
        if N >= i * 2:
            print("double", i)
            N -= i * 2
            break
    for i in range(20, -1, -1):
        if N >= i:
            print("single", i)
            N -= i
            break
    if N != 0:
        print("impossible")

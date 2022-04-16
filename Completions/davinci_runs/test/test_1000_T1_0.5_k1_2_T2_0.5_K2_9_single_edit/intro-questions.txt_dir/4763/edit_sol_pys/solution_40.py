
N = int(input())

if N < 1 or N > 180:
    print("impossible")
else:
    for i in range(20, 0, -1):  # 높이가 20인 삼각형부터 검사
        if N >= i*3:
            print("triple", i)
            N -= i*3
            break
    for i in range(20, 0, -1):  # 높이가 20인 이등변삼각형부터 검사
        if N >= i*2:
            print("double", i)
            N -= i*2
            break
    for i in range(20, 0, -1):  # 높이가 20인 직사각형부터 검사
        if N >= i:
            print("single", i)
            N -= i
            break
    if N != 0:
        print("impossible")

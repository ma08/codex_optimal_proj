
#-----Solution-----

#This is a greedy algorithm.
#The idea is to greedily multiply by 3 until the number is greater than M.
#Then, multiply by 2 as many times as possible, until the number is greater than M.
#If the number is not M, then the answer is -1.

N, M = map(int, input().split())

if N == M:
    print(0)
elif M % 2 == 0 and N % 2 == 1:
    print(-1)
else:
    steps = 0
    while N < M:
        if N * 3 <= M:
            N *= 3
        else:
            N *= 2
        steps += 1
    if N == M:
        print(steps)
    else:
        print(-1)

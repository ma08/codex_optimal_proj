

a, b = input().split()  # input
N, M = len(a), len(b)   # str length

for i in range(M):      # str b
    for j in range(N):   # str a
        if a[j] == b[i]: # compare
            print(b[i], end='')    # print b[i]
        else:
            print('.', end='')
    print()

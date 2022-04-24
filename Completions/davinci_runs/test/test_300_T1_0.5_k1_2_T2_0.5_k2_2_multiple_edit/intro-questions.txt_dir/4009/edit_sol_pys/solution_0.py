

N, X, Y = map(int, input().split())
N = str(input())

if N[Y-1] == '0':
    N = N[:Y-1] + '1' + N[Y:]
else:
    N = N[:Y-1] + '0' + N[Y:]
    for i in range(Y, X):
        if N[i-1] == '0':
            N = N[:i-1] + '1' + N[i:]
            break
        else:
            N = N[:i-1] + '0' + N[i:]

print(N.count('0'))

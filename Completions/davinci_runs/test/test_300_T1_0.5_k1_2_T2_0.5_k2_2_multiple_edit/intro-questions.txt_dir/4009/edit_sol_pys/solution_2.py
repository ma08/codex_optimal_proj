
N, X, Y = map(int, input().split())
N = list(str(input()))

if N[Y] == '0':
    N[Y] = '1'
else:
    N[Y] = '0'
    for i in range(Y+1, X):
        if N[i] == '0':
            N[i] = '1'
            break
        else:
            N[i] = '0'

print(N.count('1'))

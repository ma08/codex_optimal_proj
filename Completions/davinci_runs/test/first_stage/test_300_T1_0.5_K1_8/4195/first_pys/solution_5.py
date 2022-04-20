

#D, N = map(int, input().split())

#print((D + 1) * 100 * (N - 1) + 100)

"""
# AtCoder Beginner Contest 100
# Problem A

A, B = map(int, input().split())

if A <= 8 and B <= 8:
    print('Yay!')
else:
    print(':(')
"""

"""
# AtCoder Beginner Contest 100
# Problem B

D, N = map(int, input().split())

if N == 100:
    print((D + 1) * 100 * N)
else:
    print((D + 1) * 100 * (N - 1) + 100)
"""

"""
# AtCoder Beginner Contest 100
# Problem C

N = int(input())

total = 0

for i in range(N):
    A = int(input())
    if A % 2 == 0:
        count = 0
        while A % 2 == 0:
            A = A / 2
            count += 1
        total += count

print(total)
"""

"""
# AtCoder Beginner Contest 100
# Problem D

N, M = map(int, input().split())

X = []
Y = []
Z = []

for i in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

all_XYZ = []

for i in range(N):
    for j in range(N):
        for k in range(N):
            all_XYZ.append(X[i] + Y[j] + Z[k])

all_XYZ.sort()

print(all_XYZ[-M])
"""
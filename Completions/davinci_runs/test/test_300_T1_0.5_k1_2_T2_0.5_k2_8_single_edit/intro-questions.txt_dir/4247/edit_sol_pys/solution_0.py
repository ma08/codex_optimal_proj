# AtCoder Beginner Contest 088
# A - Infinite Coins

N = int(input())
A = int(input())

if N % 500 <= A:
    print('Yes')
else:
    print('No')


# B - Card Game for Two

N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

alice = 0
bob = 0

for i in range(N):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(alice - bob)


# C - Special Trains

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

for i in range(N):
    if a[i] >= b[i]:
        ans += b[i]
        b[i] = 0
    else:
        ans += a[i]
        b[i] -= a[i]
        a[i] = 0

    if b[i] > 0:
        if a[i + 1] >= b[i]:
            ans += b[i]
            a[i + 1] -= b[i]
        else:
            ans += a[i + 1]
            a[i + 1] = 0

print(ans)


# D - We Love Golf

N = int(input())
D = list(map(int, input().split()))

ans = sum(D)

for i in range(N):
    for j in range(i + 1, N):
        ans += D[i] * D[j]

print(ans)


# E - Go to School

from itertools import product

N, M, P, Q, R = map(int, input().split())

XYZ = [list(map(int, input().split())) for _ in range(R)]

ans = 0

for x, y, z in product(range(M), range(N), range(M)):
    if x == y or x == z or y == z:
        continue
    else:
        ans = max(ans, sum([z for x, y, z in XYZ if x == x and y == y and z == z]))

print(ans)


# F - XOR World

from itertools import permutations

N, M, K = map(int, input().split())

A = list(map(int, input().split()))



# G - All Green


n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
        count += 1
print(count)

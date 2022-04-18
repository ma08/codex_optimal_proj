# AtCoder Beginner Contest 010
# C - 浮気調査

# input
T, X = map(int, input().split())
N = int(input())
B = list(map(int, input().split()))
A = list(map(int, input().split()))

# output (WA)
for i in range(N):
    if T-B[i]*X >= 0:
        T -= B[i]*X
    else:
        print(i)
        exit()

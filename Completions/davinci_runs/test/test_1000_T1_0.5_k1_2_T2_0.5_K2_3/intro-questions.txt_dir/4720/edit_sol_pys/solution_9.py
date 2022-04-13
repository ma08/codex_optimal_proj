
N = int(input())
S = [0] * 100001
for i in range(N):
    l, r = map(int, input().split())  # l: left point, r: right point
    for j in range(l, r+1):
        S[j] = 1
print(sum(S))

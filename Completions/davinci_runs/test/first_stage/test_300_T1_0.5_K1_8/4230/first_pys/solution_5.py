

X, N = input().split()
X = int(X)
N = int(N)

P = input().split()
P = [int(i) for i in P]

#print(X, N, P)

ans = 101
for i in range(1, 101):
    if i not in P:
        if abs(X-i) < abs(X-ans):
            ans = i

print(ans)
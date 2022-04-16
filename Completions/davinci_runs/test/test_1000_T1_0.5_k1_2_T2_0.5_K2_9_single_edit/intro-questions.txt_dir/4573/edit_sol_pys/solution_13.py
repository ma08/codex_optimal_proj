
N = int(input())
X = list(map(int, input().split()))
ans = []
for i in range(1, N):
    left = X[:i]
    right = X[i:]
    ans.append(sum(left) / len(left) + sum(right) / len(right))
print(min(ans))

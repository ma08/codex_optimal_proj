

N, M = map(int, input().split())
A = list(map(int, input().split()))
print(A)

if max(A) >= sum(A) / (4 * M):
    print('Yes')
else:
    print('No')

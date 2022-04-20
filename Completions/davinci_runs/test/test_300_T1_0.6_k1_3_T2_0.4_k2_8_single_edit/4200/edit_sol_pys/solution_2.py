
N, M = map(int, input().split())
A = list(map(int, input().split()))

print('Yes' if max(A) >= sum(A) / (4 * M) else 'No')

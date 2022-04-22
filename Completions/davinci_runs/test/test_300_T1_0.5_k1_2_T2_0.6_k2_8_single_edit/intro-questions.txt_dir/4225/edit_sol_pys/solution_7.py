

N, K = map(int, input().split())
A = list(map(int, input().split()))

# N, K = 2, 3
# A = [1, 2]

print(max(A) - min(A) - 2 * K)

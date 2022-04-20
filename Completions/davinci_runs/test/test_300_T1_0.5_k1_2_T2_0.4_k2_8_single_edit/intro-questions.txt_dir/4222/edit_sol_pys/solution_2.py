

N = int(input())
A = list(map(int, input().split()))

print(N - len(set(A)))

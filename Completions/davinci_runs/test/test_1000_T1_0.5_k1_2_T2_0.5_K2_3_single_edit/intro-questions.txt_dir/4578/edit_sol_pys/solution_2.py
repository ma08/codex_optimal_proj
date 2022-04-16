

N, X = map(int, input().split())
m = [int(input()) for i in range(N)]

print(X // min(m) + (X % min(m) != 0))

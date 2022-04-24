

X, K, D = map(int, input().split())
print(min(abs(X + D * K), abs(X - D * K)))

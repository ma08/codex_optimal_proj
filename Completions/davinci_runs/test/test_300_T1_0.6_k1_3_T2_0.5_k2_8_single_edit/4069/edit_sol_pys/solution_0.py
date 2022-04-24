
X, K, D = map(int, input().split())
print(min(abs(X), abs(X + D * K), abs(X - D * K)))

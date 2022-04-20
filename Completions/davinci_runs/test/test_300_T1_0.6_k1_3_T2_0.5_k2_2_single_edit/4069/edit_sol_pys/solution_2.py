


print(min(abs(X + D * K), abs(X - D * K)))
X, K, D = map(int, input().split())

# if abs(X) > K * D:
#     print(abs(X) - K * D)
#     exit()

# if abs(K * D) % 2 == abs(X) % 2:
#     print(abs(abs(K * D) - abs(X)))
# else:
#     print(abs(abs(K * D) - abs(X)) + 1)

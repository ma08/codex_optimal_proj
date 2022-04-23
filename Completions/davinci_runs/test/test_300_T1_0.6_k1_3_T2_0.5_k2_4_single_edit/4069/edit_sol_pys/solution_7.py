N, M = map(int, input().split())
A = list(map(int, input().split()))


if N >= M:
    print(0)
    exit()

A.sort()
diff = [A[i] - A[i - 1] for i in range(1, M)]
diff.sort(reverse=True)

# if abs(K * D) % 2 == abs(X) % 2:
#     print(abs(abs(K * D) - abs(X)))
# else:
#     print(abs(abs(K * D) - abs(X)) + 1)

print(min(abs(X + D * K), abs(X - D * K)))

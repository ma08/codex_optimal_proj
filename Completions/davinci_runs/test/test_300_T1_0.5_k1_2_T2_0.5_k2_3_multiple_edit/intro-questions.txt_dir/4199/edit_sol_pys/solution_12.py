n = int(input())
x = sorted([int(input()) for _ in range(n)])
print(sum(x[i + 1] - x[i] for i in range(n - 1)) / (n - 1))


n, m = map(int, input().split())

print(2 ** (n + m) - 2 ** ((n + m) // 2) if (n + m) % 2 == 0 else 2 ** (n + m))

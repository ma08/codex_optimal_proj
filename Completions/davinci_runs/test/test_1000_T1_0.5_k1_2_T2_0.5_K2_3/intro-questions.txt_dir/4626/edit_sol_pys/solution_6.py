
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(min(abs(a - b) + abs(c - d), abs(a - c) + abs(b - d), abs(a - d) + abs(b - c)))

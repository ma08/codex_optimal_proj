

a, b, c, d = map(int, input().split(' ')) # a, b, c, d = (int(input()) for _ in range(4))
print(max(0, min(b, d) - max(a, c)))

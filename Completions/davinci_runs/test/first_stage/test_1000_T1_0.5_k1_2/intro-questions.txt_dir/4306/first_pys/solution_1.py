

# input
a, b, c, d = map(int, input().split())

# output
print(max(0, min(b, d) - max(a, c)))
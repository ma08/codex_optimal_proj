

n, a, b, c, d, e = map(int, input().split())

l = [a, b, c, d, e]
print(n//min(l) + 1 if n%min(l) != 0 else n//min(l))
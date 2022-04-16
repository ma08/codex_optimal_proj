

a, b = input().split()
print(a[::-1] if a[::-1] > b[::-1] else b[::-1])

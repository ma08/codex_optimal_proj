

a, b = map(int, input().split())

print(min(a+b+a, a+b+b, b+a+b, b+a+a))

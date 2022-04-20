

a, b, c = (int(x) for x in input().split())

print(min(a+b+c, a+2*b+2*c, 2*a+b+2*c, 2*a+2*b+3*c))
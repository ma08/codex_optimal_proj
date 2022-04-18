
a, b = map(int, input().split())

if a % 10**b >= 5*10**(b-1):
    print(a + (10**b - a % 10**b))
else:
    print(a - a % 10**b)

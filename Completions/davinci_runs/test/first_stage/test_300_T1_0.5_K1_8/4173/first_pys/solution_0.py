

# SOLUTION
q = int(input())
for i in range(q):
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if n % 2 == 0:
        print((n//2)*a)
    else:
        print(min(((n//2)*a)+a, ((n//2)*a)+b))
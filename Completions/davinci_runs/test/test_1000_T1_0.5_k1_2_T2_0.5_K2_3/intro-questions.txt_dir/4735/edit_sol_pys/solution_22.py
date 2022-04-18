

a, b, c, d = map(int, input().split())

if a == c or b == d or abs(a - c) == abs(b - d):
    print("YES")
else: 
    print("NO")

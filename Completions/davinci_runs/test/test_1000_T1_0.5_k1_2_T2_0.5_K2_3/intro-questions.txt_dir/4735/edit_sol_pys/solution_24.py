

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == c or b == d:
    print("YES")
elif abs(a - c) == abs(b - d):
    print("YES")
else:
    print("NO")

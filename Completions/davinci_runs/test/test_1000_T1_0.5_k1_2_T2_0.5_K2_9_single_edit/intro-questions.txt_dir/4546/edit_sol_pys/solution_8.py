

a, b = map(int, input().split())
if a % 2 == 0:
    if b % 2 == 0:
        print("NO")
    else:
        print("YES")
else:
    if b % 2 == 0:
        print("YES")
    else:
        print("NO")



a, b, c = map(int, input().split())

if a * b * c == 0:
    print("YES")
else:
    if a + b == c:
        print("YES")
    elif a - b == c:
        print("YES")
    elif a * b == c:
        print("YES")
    elif a / b == c:
        print("YES")
    elif b + c == a:
        print("YES")
    elif b - c == a:
        print("YES")
    elif b * c == a:
        print("YES")
    elif b / c == a:
        print("YES")
    else:
        print("NO")

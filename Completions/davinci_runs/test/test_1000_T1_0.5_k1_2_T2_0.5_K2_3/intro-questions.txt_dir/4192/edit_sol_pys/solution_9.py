

a, b, c = map(int, input().split())
if a % c == 0:
    if a / c <= b:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")

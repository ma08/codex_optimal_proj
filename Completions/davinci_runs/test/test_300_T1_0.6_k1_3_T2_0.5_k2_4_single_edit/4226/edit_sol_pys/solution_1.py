

x, y = map(int, input().split())

if y % 2 == 0:
    if y / 2 >= x:
        print("Yes")
    else:
        print("No")
else:
    print("No")

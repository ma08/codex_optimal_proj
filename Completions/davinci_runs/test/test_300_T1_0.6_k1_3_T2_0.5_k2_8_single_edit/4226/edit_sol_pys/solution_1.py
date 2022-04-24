
x, y = map(int, input().split())

if y % 2 == 0 and y / 2 >= x and y >= 2 * x:
    print("Yes")
else:
    print("No")

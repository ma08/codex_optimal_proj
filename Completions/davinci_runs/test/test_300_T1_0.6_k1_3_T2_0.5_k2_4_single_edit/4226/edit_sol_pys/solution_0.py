

x, y = map(int, input().split())
if y % 2 == 0 and 4 * x <= y <= 2 * x:
    print("Yes")
else:
    print("No")

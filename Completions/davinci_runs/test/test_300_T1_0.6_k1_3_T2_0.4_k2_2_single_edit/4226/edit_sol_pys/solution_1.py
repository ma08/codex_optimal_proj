
x, y = map(int, input().split())

if y % 2 == 0 and y / 2 >= x: # yが偶数で、xよりy/2が大きい場合
    print("Yes")
else:
    print("No")



x, y = map(int, input().split()) #x,yを分割して整数型に変換

if y % 2 == 0 and x * 2 <= y and y <= x * 4:
    print("Yes")
else:
    print("No")

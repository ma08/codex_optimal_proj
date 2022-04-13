

x1, y1, x2, y2 = map(int, input().split())  # getting input from the user

if x1 == x2:  # if x1 = x2
    x3 = x1 + abs(y1 - y2)
    x4 = x1 - abs(y1 - y2)
    y3 = y1
    y4 = y2
elif y1 == y2:  # if y1 = y2
    x3 = x1
    x4 = x2
    y3 = y1 + abs(x1 - x2)
    y4 = y1 - abs(x1 - x2)
else:  # if x1 != x2 and y1 != y2
    x3 = x2
    y3 = y1
    x4 = x1
    y4 = y2

print(x3, y3, x4, y4)  # printing the output

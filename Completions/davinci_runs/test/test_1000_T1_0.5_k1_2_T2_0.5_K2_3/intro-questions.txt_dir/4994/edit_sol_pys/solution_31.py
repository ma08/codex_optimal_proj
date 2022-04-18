
# Read input
XY = []
for i in range(3):
    XY.append([int(i) for i in input().split()])

# Find the missing point by comparing the points
for i in range(3):
    for j in range(3):
        if XY[i][0] == XY[j][0] and XY[i][1] != XY[j][1]:
            x = XY[i][0]
            y = XY[i][1] + XY[j][1] - XY[i][1]
        elif XY[i][1] == XY[j][1] and XY[i][0] != XY[j][0]:
            x = XY[i][0] + XY[j][0] - XY[i][0]
            y = XY[i][1]
        if 'x' in locals() and 'y' in locals():
            print(x, y)
            break
    if 'x' in locals() and 'y' in locals():
        break

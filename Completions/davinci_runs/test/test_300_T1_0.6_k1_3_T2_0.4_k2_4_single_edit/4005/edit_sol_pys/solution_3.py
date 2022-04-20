
#This solution is wrong because it does not take into account the situation when the rectangle is rotated

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

x5 = int(input())
y5 = int(input())
x6 = int(input())
y6 = int(input())

x_list = [x1,x2,x3,x4,x5,x6]
y_list = [y1,y2,y3,y4,y5,y6]

x_list.sort()
y_list.sort()

x_max = x_list[-1]
x_min = x_list[0]
y_max = y_list[-1]
y_min = y_list[0]

flag = True

for i in range(x_min,x_max+1):
    for j in range(y_min,y_max+1):
        if x_min<i<x_max and y_min<j<y_max:
            flag = False

if flag:
    print("YES")
else:
    print("NO")

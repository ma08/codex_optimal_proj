# This solution is wrong

x_list = []
y_list = []
for _ in range(6):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_list.sort()
y_list.sort()

x_max = x_list[-1]
x_min = x_list[0]
y_max = y_list[-1]
y_min = y_list[0]

flag = True

for i in range(x_min, x_max+1):
    for j in range(y_min, y_max+1):
        if x_min < i < x_max and y_min < j < y_max:
            flag = False

if flag:
    print("YES")
else:
    print("NO")

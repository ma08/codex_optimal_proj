n = int(input())
t_list = [0]
x_list = [0]
y_list = [0]
for i in range(n):
    t, x, y = map(int, input().split())
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)

for i in range(n):
    d = t_list[i + 1] - (abs(x_list[i + 1] - x_list[i]) + abs(y_list[i + 1] - y_list[i]))
    if d < 0 or d % 2 != 0:
        print("No")
        exit()
print("Yes")

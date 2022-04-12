n = int(input())
t_list = [0]
x_list = [0]
y_list = [0]
for i in range(n):
    t, x, y = map(int, input().split())
    t_list.append(t_list[i] + t)
    x_list.append(x_list[i] + x)
    y_list.append(y_list[i] + y)

for i in range(1, n + 1):
    d = t_list[i] - (abs(x_list[i] - x_list[i - 1]) + abs(y_list[i] - y_list[i - 1]))
    if d < 0 or d % 2 != 0:
        print("No")
        exit()
print("Yes")

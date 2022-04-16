

n = int(input())
t_list = []
x_list = []
y_list = []
for i in range(n):
    t, x, y = map(int, input().split())
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)

for i in range(n):
    d = t_list[i] - (abs(x_list[i] - x_list[i - 1]) + abs(y_list[i] - y_list[i - 1]))
    if d < 0 or d % 2 != 0:
        print("No")
        exit()
print("Yes")
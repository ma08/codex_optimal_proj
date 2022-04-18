

n = int(input())
t_list = []
x_list = []
y_list = []
for i in range(n):
    t, x, y = map(int, input().split())
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)

for i in range(1, n):
    d = t_list[i] - (abs(x_list[i]) + abs(y_list[i]))
    if d < 0 or d % 2 != 0:
        print("No")
        exit()
print("Yes")

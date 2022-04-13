

def main():
    n = int(input())
    t_list = []
    x_list = []
    y_list = []
    for i in range(n):
        t, x, y = map(int, input().split())
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
    x = 0
    y = 0

for i in range(n):
    d = t_list[i] - (abs(x_list[i] - x) + abs(y_list[i] - y))
    if d < 0 or d % 2 != 0:
        print("No")
        exit()
print("Yes")

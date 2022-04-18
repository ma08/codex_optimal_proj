

n, m, x, y = map(int, input().split())
x_list = [int(i) for i in input().split()]
y_list = [int(i) for i in input().split()]

x_list.sort()
y_list.sort()

for i in range(x, y + 1):
    if x_list[-1] < i and y_list[0] >= i:
        print('No War')
        exit()
print('War')

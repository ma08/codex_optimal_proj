
n, m, x, y = map(int, input().split())
x_list = sorted([int(i) for i in input().split()])
y_list = sorted([int(i) for i in input().split()])

if x_list[-1] >= y_list[0]:
    print('War')
    exit()

for i in range(x_list[-1], y_list[0]):
    if i <= x and i <= y:
        print('No War')
        exit()

print('War')

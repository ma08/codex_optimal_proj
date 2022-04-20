

n, m, x, y = map(int, input().split())
x_list = [int(i) for i in input().split()]
y_list = [int(i) for i in input().split()]

if max(x_list) >= min(y_list):
    print('War')
else:
    print('No War')

import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())
x_list = [int(i) for i in input().split()]
y_list = [int(i) for i in input().split()]

x_list.sort()
y_list.sort()

if x_list[-1] >= y_list[0]:
    print('War')
else:
    print('No War')

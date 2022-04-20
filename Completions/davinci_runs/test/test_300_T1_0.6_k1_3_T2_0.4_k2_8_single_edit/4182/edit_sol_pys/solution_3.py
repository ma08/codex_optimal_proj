

n, m, x, y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

for i in range(x+1, y):
    if all(x_list[j] < i for j in range(n)) and all(y_list[j] >= i for j in range(m)):  # all(x_list[j] < i for j in range(n))はx_list[0] < i and x_list[1] < i and ... and x_list[n-1] < i
        print('No War')
        exit(0)
print('War')

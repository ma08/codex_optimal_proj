

# Get input
n, m, x, y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

# Check if war will break out
if x < y:
    for z in range(x + 1, y + 1):
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):
            print('No War')
            break
    else:
        print('War')
else:
    print('War')
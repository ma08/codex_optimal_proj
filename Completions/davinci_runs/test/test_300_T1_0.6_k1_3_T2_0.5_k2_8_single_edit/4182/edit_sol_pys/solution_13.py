

n, m, x, y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

for i in range(x+1, y):
    if all(x_list[j] < i for j in range(n)) and all(y_list[j] >= i for j in range(m)):  # x_list[j] < i がn個全てTrue or y_list[j] >= i がm個全てTrue
        print('No War')
        exit(0)
print('War')

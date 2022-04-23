
n = int(input())

coord_dict = {}
for i in range(n):
    x, y, h = map(int, input().split())
    coord_dict[(x, y)] = h

for x in range(101):
    for y in range(101):
        h = -1
        for (x_, y_), h_ in coord_dict.items():
            if h == -1 or h == h_ + abs(x - x_) + abs(y - y_):
                h = h_ + abs(x - x_) + abs(y - y_)
            else:
                break
        else:
            print(x, y, h)
            exit()

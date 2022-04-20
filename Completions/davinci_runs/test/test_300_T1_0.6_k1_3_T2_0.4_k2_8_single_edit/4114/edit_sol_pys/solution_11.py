n = int(input())
h_list = []
for i in range(n):
    x, y, h = map(int, input().split())
    h_list.append((x, y, h))


for cx in range(101):
    for cy in range(101):
        h = 0
        for x, y, h_ in h_list:
            if h_ > 0:
                h = h_ + abs(cx - x) + abs(cy - y)
        if all(h_ == max(h - abs(cx - x) - abs(cy - y), 0) for x, y, h_ in h_list):
            print(cx, cy, h)
            exit(0)

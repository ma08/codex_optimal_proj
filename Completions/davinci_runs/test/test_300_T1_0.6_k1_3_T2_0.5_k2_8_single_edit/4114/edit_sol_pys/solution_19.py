# -*- coding: utf-8 -*-

n = int(input())

coord_dict = {}
for i in range(n):
    x, y, h = map(int, input().split())
    coord_dict[(x, y)] = h

for x in range(101):
    for y in range(101):
        h = -1
        for (x_, y_), h_ in coord_dict.iteritems():
            if h == -1:
                h = h_ + abs(x - x_) + abs(y - y_)
            elif h != h_ + abs(x - x_) + abs(y - y_):
                break
        else:
            print(x, y, h)
            exit()

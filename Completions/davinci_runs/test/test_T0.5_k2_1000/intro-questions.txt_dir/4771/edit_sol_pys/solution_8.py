
n, V = [int(x) for x in input().split()]
largest_box = 0
for i in range(n):
    l, w, h = [int(x) for x in input().split()]
    volume = l*w*h
    if volume > largest_box:
        largest_box = volume

print(largest_box - V)

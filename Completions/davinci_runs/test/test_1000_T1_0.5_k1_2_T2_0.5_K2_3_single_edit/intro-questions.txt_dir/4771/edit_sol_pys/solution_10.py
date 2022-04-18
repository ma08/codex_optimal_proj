
n, V = map(int, input().split())
largest_box = 0
for i in range(n):
    l, w, h = map(int, input().split())
    volume = l*w*h
    if volume > largest_box:
        largest_box = volume

print(largest_box - V)

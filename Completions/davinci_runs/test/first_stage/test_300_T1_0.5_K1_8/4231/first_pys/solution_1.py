

h, w = map(int, input().split())
a, b = map(int, input().split())
print(h*w - (h-a)*w - (w-b)*h + (h-a)*(w-b))
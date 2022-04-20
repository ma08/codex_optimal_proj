

h, w = map(int, input().split())
h_, w_ = map(int, input().split())
print(h*w - (h-h_)*w - (w-w_)*h + (h-h_)*(w-w_))
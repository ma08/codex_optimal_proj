
w,h,n = map(int,input().split())

x_max = w
x_min = 0
y_max = h
y_min = 0

for i in range(n):
    x,y,a = map(int,input().split())
    if a == 1:
        x_min = max(x_min,x)
    elif a == 2:
        x_max = min(x_max,x)
    elif a == 3:
        y_min = max(y_min,y)
    elif a == 4:
        y_max = min(y_max,y)

if x_min > x_max or y_min > y_max:
    print(0)
else:
    print((x_max-x_min)*(y_max-y_min))


#---------------------------------------------------------------------------------------------------------------
t = int(input())
for i in range(t):
    h, m = map(int, input().split())
    h = 24 - h
    if m != 0:
        h -= 1
        m = 60 - m
    else:
        h -= 1
    print(h*60 + m)

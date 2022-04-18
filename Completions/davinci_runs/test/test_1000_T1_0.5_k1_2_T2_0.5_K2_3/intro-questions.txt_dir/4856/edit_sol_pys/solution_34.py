

#-----main----- 
a, b = map(int, input().split())

if a[::-1] > b[::-1]:
    print(a[::-1], end="")
else:
    print(b[::-1], end="")

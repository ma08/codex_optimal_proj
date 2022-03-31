

a,b,c,d = map(int,input().split())

max_value = a*c
if a*d > max_value:
    max_value = a*d
if b*c > max_value:
    max_value = b*c
if b*d > max_value:
    max_value = b*d

print(max_value)

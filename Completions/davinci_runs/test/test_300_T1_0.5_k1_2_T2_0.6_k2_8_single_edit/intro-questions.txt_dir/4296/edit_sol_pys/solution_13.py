

a,b,c,d = map(int, input().split())

if a+b == c+d:
    print('Balanced')
else:
    print('Left') if a+b > c+d else print('Right')

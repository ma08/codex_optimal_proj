a,b = map(int, input().split())


if a%2 == 0:
    print(a*b)
else:
    print(a*(b-1)+a)

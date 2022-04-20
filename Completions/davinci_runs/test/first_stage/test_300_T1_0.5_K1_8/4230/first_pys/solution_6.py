

x, n = map(int, input().split())
p = list(map(int, input().split()))

if x not in p:
    print(x)
else:
    for i in range(101):
        if x-i not in p:
            print(x-i)
            break
        if x+i not in p:
            print(x+i)
            break
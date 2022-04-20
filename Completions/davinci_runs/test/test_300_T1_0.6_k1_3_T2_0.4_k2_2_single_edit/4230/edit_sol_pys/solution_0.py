
x, n = map(int, input().split())
p = set(map(int, input().split()))

for i in range(0, 200): # 200 is too large
    if x - i not in p:
        print(x - i)
        exit()
    elif x + i not in p:
        print(x + i)
        exit()

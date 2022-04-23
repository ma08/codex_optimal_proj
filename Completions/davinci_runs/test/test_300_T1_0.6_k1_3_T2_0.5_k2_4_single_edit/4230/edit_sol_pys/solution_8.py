
x, n = map(int, input().split())
p = set(map(int, input().split()))

for i in range(0, 200):
    if x - i not in p:
        print(x - i)
        exit()
    elif x + i not in p:
        print(x + i)
        exit()

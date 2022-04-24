

x, n = map(int, input().split())  # x:int, n:int
p = set(map(int, input().split()))  # p: int list

for i in range(0, 200):  # 0 <= i < 200
    if x - i not in p:
        print(x - i)
        exit()
    elif x + i not in p:
        print(x + i)
        exit()

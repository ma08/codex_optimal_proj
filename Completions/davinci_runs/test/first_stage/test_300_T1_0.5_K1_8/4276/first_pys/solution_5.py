

n, t = map(int, input().split())

for i in range(n):
    c, ti = map(int, input().split())
    if ti <= t:
        print(c)
        break
else:
    print('TLE')
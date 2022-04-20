

n, t = map(int, input().split())
c = []
for _ in range(n):
    c.append(list(map(int, input().split())))

c.sort(key=lambda x: x[0])

for i in range(n):
    if c[i][1] <= t:
        print(c[i][0])
        exit()
print('TLE')
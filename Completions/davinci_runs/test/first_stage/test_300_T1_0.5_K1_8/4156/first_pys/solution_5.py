

n, w = map(int, input().split())
a = list(map(int, input().split()))

if n == 1:
    print(w+1)
    exit()

if a[0] == 0:
    print(w+1)
    exit()

if a[0] > 0 and a[1] > 0:
    print(0)
    exit()

if a[0] < 0 and a[1] < 0:
    print(0)
    exit()

d = {}

for i in range(n):
    if a[i] in d.keys():
        print(0)
        exit()
    if a[i] > 0:
        d[a[i]] = 1
    else:
        d[-a[i]] = -1

# print(d)

cnt = 0

for i in range(1, w+1):
    if i in d.keys():
        s = d[i]
    else:
        s = 0
    if i-1 in d.keys():
        s += d[i-1]
    if i+1 in d.keys():
        s += d[i+1]
    if s == 0:
        cnt += 1

print(cnt)
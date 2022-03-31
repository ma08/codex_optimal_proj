

n = int(input())

a = list(map(int, input().split()))

neg = []
pos = []

for i in a:
    if i < 0:
        neg.append(i)
    elif i > 0:
        pos.append(i)
    else:
        pass

cnt = 0

if len(neg) % 2 == 0:
    cnt = 0
else:
    cnt = 1

print(cnt + len(pos) + len(neg))
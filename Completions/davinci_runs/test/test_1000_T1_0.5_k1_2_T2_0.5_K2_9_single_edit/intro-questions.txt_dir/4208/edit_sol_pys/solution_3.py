
# -*- coding: utf-8 -*-


n = int(input())
l = input()
r = input()

left = []
right = []

for i in range(n):
    if l[i] == '?':
        left.append((i, '?'))
    else:
        left.append((i, l[i]))

for i in range(n):
    if r[i] == '?':
        right.append((i, '?'))
    else:
        right.append((i, r[i]))

left.sort(key=lambda x: x[1])
right.sort(key=lambda x: x[1])

ans = 0

for i in range(n):
    if left[i][1] == '?':
        break
    for j in range(n):
        if right[j][1] == '?':
            break
        if left[i][1] == right[j][1]:
            ans += 1
            del left[i]
            del right[j]
            break

left.sort(key=lambda x: x[0])
right.sort(key=lambda x: x[0])

print(ans)

for i in range(ans):
    print(left[i][0] + 1, right[i][0] + 1)

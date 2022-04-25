
n = int(input())
l = input()
r = input()

leftt = []
right = []

for i in range(n):
    if l[i] == '?':
        leftt.append((i, '?'))
    else:
        leftt.append((i, l[i]))

for i in range(n):
    if r[i] == '?':
        right.append((i, '?'))
    else:
        right.append((i, r[i]))

leftt.sort(key=lambda x: x[1])
right.sort(key=lambda x: x[1])

ans = 0

for i in range(n):
    if leftt[i][1] == '?':
        break
    for j in range(n):
        if right[j][1] == '?':
            break
        if leftt[i][1] == right[j][1]:
            ans += 1
            del leftt[i]
            del right[j]
            break

leftt.sort(key=lambda x: x[0])
right.sort(key=lambda x: x[0])

print(ans)

for i in range(ans*2):
    print(leftt[i][0] + 1, right[i][0] + 1)



n = int(input())
l = input()
r = input()

left = [0] * n
right = [0] * n

for i in range(n):
    if l[i] == '?':
        left[i] = ('?', i)
    else:
        left[i] = (l[i], i)

for i in range(n):
    if r[i] == '?':
        right[i] = ('?', i)
    else:
        right[i] = (r[i], i)

left.sort(key=lambda x: x[1])
right.sort(key=lambda x: x[1])

ans = 0

for i in range(n):
    if left[i][0] == '?':
        break
    for j in range(n):
        if right[j][0] == '?':
            break
        if left[i][0] == right[j][0]:
            ans += 1
            del left[i]
            del right[j]
            break

left.sort(key=lambda x: x[0])
right.sort(key=lambda x: x[0])

print(ans)

for i in range(ans):
    print(left[i][0] + 1, right[i][0] + 1)

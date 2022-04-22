
n = int(input())
l = input()
r = input()

left = []
right = []

for i in range(n):
    if l[i] == '?':
        left.append((i, '?'))
    else:
        left.append((i, int(l[i])))

for i in range(n):
    if r[i] == '?':
        right.append((i, '?'))
    else:
        right.append((i, int(r[i])))

left.sort(key=lambda x: x[1])
right.sort(key=lambda x: x[1])

left = list(filter(lambda x: x[1] != '?', left))
right = list(filter(lambda x: x[1] != '?', right))

ans = 0

for i in range(len(left)):
    for j in range(len(right)):
        if left[i][1] == right[j][1]:
            if left[i] not in left[i + 1:] and right[j] not in right[j + 1:]:
                ans += 1
                left[i] = '*'
                right[j] = '*'
                break

left = list(filter(lambda x: x != '*', left))
right = list(filter(lambda x: x != '*', right))

left.sort(key=lambda x: x[0])
right.sort(key=lambda x: x[0])

print(ans)

for i in range(ans):
    print(left[i][0] + 1, right[i][0] + 1)

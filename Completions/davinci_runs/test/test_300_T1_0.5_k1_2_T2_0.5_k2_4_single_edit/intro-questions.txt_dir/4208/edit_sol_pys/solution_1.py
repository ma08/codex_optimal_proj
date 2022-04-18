
n = int(input())
l = input()
r = input()

l = list(enumerate(l))
r = list(enumerate(r))

l.sort(key=lambda x: x[1])
r.sort(key=lambda x: x[1])

left = [x for x in l if x[1] != '?']
right = [x for x in r if x[1] != '?']

ans = 0

for i in range(n):
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

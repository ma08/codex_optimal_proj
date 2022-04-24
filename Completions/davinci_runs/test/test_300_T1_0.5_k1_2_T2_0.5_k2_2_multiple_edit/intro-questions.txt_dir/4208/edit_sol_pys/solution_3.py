

n = int(input()) # 4
l = input() # ?a?b?
r = input() # a?b??

left = [] # [(0,'?'), (1,'a'), (2,'?'), (3,'b')]
right = [] # [(0,'a'), (1,'?'), (2,'b'), (3,'?'), (4,'?')]

for i in range(n):
    left.append((i, l[i])) # (0, '?'), (1, 'a'), (2, '?'), (3, 'b')
    right.append((i, r[i])) # (0, 'a'), (1, '?'), (2, 'b'), (3, '?'), (4, '?')

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


n = int(input())
l = input()
r = input()

l_list = []
r_list = []

for i in range(n):
    if l[i] == '?':
        l_list.append((i, '?'))
    else:
        l_list.append((i, l[i]))

for i in range(n):
    if r[i] == '?':
        r_list.append((i, '?'))
    else:
        r_list.append((i, r[i]))

l_list.sort(key=lambda x: x[1])
r_list.sort(key=lambda x: x[1])

ans = 0

for i in range(n):
    if l_list[i][1] == '?':
        break
    for j in range(n):
        if r_list[j][1] == '?':
            break
        if l_list[i][1] == r_list[j][1]:
            ans += 1
            del l_list[i]
            del r_list[j]
            break

l_list.sort(key=lambda x: x[0])
r_list.sort(key=lambda x: x[0])

print(ans)

for i in range(ans):
    print(l_list[i][0] + 1, r_list[i][0] + 1)

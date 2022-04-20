

n, m = map(int, input().split())

switches = [[] for _ in range(n)]
bulbs = [0] * m

for i in range(m):
    temp = list(map(int, input().split()))
    bulbs[i] = temp[0]
    for j in range(1, temp[0] + 1):
        switches[temp[j] - 1].append(i)

bulb_states = list(map(int, input().split()))

ans = 0

for i in range(2 ** n):
    on_switches = []
    for j in range(n):
        if (i >> j) & 1:
            on_switches.append(j)

    flag = True

    for k in range(m):
        cnt = 0
        for j in on_switches:
            if k in switches[j]:
                cnt += 1

        if cnt % 2 != bulb_states[k]:
            flag = False
            break

    if flag:
        ans += 1

print(ans)
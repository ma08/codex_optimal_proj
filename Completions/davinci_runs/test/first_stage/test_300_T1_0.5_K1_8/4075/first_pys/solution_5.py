

N, M = map(int, input().split())

switches = [[] for i in range(N + 1)]
for i in range(M):
    k, *s = map(int, input().split())
    switches[k].append(s)

p = list(map(int, input().split()))

# print(switches)
# print(p)

def check(s):
    for i, c in enumerate(s):
        # print(i, c)
        # print(switches[i + 1])
        # print([(1 if j in c else 0) for j in switches[i + 1]])
        # print(list(map(lambda x: 1 if x in c else 0, switches[i + 1])))
        if sum(1 if j in c else 0 for j in switches[i + 1]) % 2 != p[i]:
            return False
    return True

count = 0
for i in range(1 << N):
    c = set()
    for j in range(N):
        if i & (1 << j):
            c.add(j + 1)
    if check(c):
        count += 1

print(count)
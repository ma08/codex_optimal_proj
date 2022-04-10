
def find(n, m, d):
    d[n] = 0
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == m:
            return d[x]
        if x * 2 <= m:
            if x * 2 not in d:
                queue.append(x * 2)
                d[x * 2] = d[x] + 1
        if x * 3 <= m:
            if x * 3 not in d:
                queue.append(x * 3)
                d[x * 3] = d[x] + 1
    return -1


n, m = map(int, input().split())
d = {}
print(find(n, m, d))

n, m = map(int, input().split())

if n == m:
    print(0)
    exit()

if m % n:
    print(-1)
    exit()

count = 0
while m != n:
    if m % 2 and m % 3:
        print(-1)
        exit()
    elif m % 2 == 0:
        m //= 2
    else:
        m //= 3
    count += 1

print(count)

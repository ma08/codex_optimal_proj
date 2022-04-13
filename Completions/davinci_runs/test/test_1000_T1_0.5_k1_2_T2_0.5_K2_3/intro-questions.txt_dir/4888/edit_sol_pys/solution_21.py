n, t = map(int, input().split())
tasks = list(map(int, input().split()))
d = {}

for i in range(n):
    if tasks[i] in d:
        d[tasks[i]].append(i)
    else:
        d[tasks[i]] = [i]

for key in d:
    print(key, d[key])

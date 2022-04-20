

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    lr = [a[0]]
    rl = [a[n-1]]
    for i in range(1, n):
        if a[i] > lr[-1]:
            lr.append(a[i])
    for i in range(n-2, -1, -1):
        if a[i] > rl[-1]:
            rl.append(a[i])
    print(max(len(lr), len(rl)))
    if len(lr) > len(rl):
        print("L"*len(lr))
    else: print("R"*len(rl))

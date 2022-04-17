

n = int(input())
a = list(map(int, input().split()))

b = [0] * n
for i in range(n):
    if i == 0:
        if a[i] != 0:
            print(-1)
            exit()
        else:
            continue
    if a[i] > a[i - 1] + 1:
        print(-1)
        exit()
    if a[i] == a[i - 1] + 1:
        b[i] = b[i - 1] + 1
    else:
        b[i] = b[i - 1]

print(sum(b))

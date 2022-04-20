

n, m = map(int, input().split())  # input n and m
a = list(map(int, input().split()))  # input a

a.sort()  # sort a

if a[-1] > n:  # check if a[-1] > n
    print(-1)
    exit()

s = 0  # initialize s
for i in range(m):
    s += a[i]  # add a[i] to s

print(n - s)  # print n - s

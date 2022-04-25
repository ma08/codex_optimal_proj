

n = int(input())
d = list(map(int, input().split()))

d.sort(reverse=True)

cnt = 0
for i in range(n//2):
    if d[i] == d[i+n//2]:
        cnt += 1
    else:
        break


# https://atcoder.jp/contests/abc086/tasks/arc089_a

n = int(input())
t = [0]
x = [0]
y = [0]

for i in range(n):
    tt, xx, yy = map(int, input().split())
    t.append(tt)
    x.append(xx)
    y.append(yy)

for i in range(n):
    dt = t[i+1] - t[i]
    dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
    if dt < dist:
        print("No")
        exit()
    if dist % 2 != dt % 2:
        print("No")
        exit()

print("Yes")


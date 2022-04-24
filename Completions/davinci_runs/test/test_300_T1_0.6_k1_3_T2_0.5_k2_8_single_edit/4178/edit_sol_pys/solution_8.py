

n = int(input())
h = list(map(int, input().split()))

ans = True
for i in range(1, n):
    if h[i - 1] > h[i]:
        h[i] = h[i - 1]
    elif h[i - 1] + 1 < h[i] or h[i - 1] == h[i]:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")

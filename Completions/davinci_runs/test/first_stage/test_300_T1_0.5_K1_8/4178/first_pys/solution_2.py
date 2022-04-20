

n = int(input())
h = list(map(int, input().split()))

h.insert(0, 0)
for i in range(1, n + 1):
    if h[i] < h[i - 1]:
        h[i] = h[i - 1]

print("Yes" if h[-1] == h[-2] else "No")
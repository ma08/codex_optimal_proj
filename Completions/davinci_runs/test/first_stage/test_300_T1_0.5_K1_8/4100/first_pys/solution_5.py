

# ---- solution ----

n, k, q = map(int, input().split())
a = [int(input()) for i in range(q)]

l = [k] * n
for i in a:
    l[i-1] += 1

for i in l:
    if i > 0:
        print("Yes")
    else:
        print("No")
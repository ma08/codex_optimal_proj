
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if a[i] + b[j] == k:
            print("YES")
            break
    else:
        continue
else:
    print("NO")

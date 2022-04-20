


n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if i + 1 == a[i]:
        continue
    else:
        if i + 1 == a[a[i] - 1]:
            print("YES")
            exit()

print("NO")

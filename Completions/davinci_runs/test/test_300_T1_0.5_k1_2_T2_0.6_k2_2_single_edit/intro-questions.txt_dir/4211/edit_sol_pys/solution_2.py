n = int(input())
a = list(map(int, input().split()))


ans = []

for i in range(n-1):
    if a[i] < a[i+1]:
        ans.append(a[i])
    else:
        ans.append(a[i+1])

ans.append(a[n-2])

print(sum(ans))

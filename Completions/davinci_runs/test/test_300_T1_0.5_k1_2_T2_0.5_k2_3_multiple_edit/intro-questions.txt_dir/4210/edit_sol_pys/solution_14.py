
# Solution 1
n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(n):
        if i != j:
            num = str(a[i]) + str(a[j])
            num = int(num)
            if num % k == 0:
                res += 1

print(res)

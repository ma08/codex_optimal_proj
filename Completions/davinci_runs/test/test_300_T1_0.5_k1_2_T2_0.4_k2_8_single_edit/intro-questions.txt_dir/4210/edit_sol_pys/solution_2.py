
# Solution 1
n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(n):
        if i != j:
            num1 = str(a[i]) + str(a[j])
            num1 = int(num1)
            if num1 % k == 0:
                res += 1

print(res)

# Solution 2
n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i + 1, n):
        num1 = str(a[i]) + str(a[j])
        num1 = int(num1)
        if num1 % k == 0:
            res += 1

print(res)

# Solution 3
n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % k == 0:
            res += 1

print(res)

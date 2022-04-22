

# Solution 1
n, k = map(int, input().split())  # O(n)
a = list(map(int, input().split()))

res = 0
for i in range(n):  # O(n)
    for j in range(n):  # O(n)
        if i != j:
            num1 = str(a[i]) + str(a[j])  # O(n)
            num1 = int(num1)  # O(n)
            if num1 % k == 0:
                res += 1

print(res)

# Solution 2
n, k = map(int, input().split())  # O(n)
a = list(map(int, input().split()))

res = 0
for i in range(n):  # O(n)
    for j in range(i + 1, n):  # O(n)
        num1 = str(a[i]) + str(a[j])  # O(n)
        num1 = int(num1)  # O(n)
        if num1 % k == 0:
            res += 1

print(res)

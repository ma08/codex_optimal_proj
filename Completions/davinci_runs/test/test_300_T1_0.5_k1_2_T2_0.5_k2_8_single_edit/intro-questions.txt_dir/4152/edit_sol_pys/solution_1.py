
# Solution

n = int(input())
arr = list(map(int, input().split()))

s = set(arr)

res = 0
for i in range(n):
    if arr[i] in s:
        res += 1
        s.remove(arr[i])

print(res)

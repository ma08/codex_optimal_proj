
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

# print(arr)

res = [0] * m

for i in range(n):
    left, right = arr[i], arr[i] + m - 1

    # print(left, right)

    if left < 0:
        left = 0

    if right > m - 1:
        right = m - 1

    res[left] = 1
    res[right] = -1


# print(res)

for i in range(1, m):
    res[i] += res[i - 1]

# print(res)

print(res.count(0))

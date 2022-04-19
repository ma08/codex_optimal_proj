# n, m = map(int, input().split())
# a = list(map(int, input().split()))


# a.sort()

# cups = 0
# pages = 0
# days = 0

# while cups < n:
#     pages += a[cups]
#     days += 1
#     cups += 1
#     if pages >= m:
#         break
#     if cups < n:
#         pages -= days - 1

# if pages < m:
#     days = -1

# print(days)

n = int(input())

arr = list(map(int, input().split()))

max_value = max(arr)

while max_value in arr:
    arr.remove(max_value)

print(max(arr))

import sys

n, k = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))  # h: 高さ

# result = 0
# for i in h:
#     if i >= k:
#         result += 1
# print(result)

for i in h:
    if i >= K:
        result += 1
print(result)

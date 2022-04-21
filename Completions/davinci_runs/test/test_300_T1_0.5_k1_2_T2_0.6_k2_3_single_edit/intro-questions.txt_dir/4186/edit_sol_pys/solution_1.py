from collections import Counter


# n = int(input())
# a = list(map(int, input().split()))

# d = {}
# for i in a:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# ans = 0
# for i in d:
#     ans += d[i] - 2

# print(ans)

n = int(raw_input())
a = map(int, raw_input().split())

c = Counter(a)

print sum(v - 2 for v in c.values())

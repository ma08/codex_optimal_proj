

# n = int(input())
# d_list = list(map(int, input().split()))

# s = 0
# for i in range(n):
#     for j in range(i+1, n):
#         s += d_list[i] * d_list[j]

# print(s)

n = int(input())
d_list = [int(input()) for _ in range(n)]

ans = 0
for d1, d2 in zip(d_list, d_list[1:]):
    ans += d1 * d2

print(ans)

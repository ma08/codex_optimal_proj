

n = int(input())

p = list(map(int, input().split()))

p.sort()

print(sum(p[:-1]) + p[-1] // 2)

# if k > n or k == 0:
#     print(-1)
# else:
#     print(n - k)

# if k > n or k == 0:
#     print(-1)
# else:
#     print(n - k)



n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

if k == 1:
    print(0)
    exit()

# a = [x // 2 for x in a]

# print(a)

# ans = 0
# while len(set(a)) != 1:
#     ans += 1
#     a = [x // 2 for x in a]

# print(ans)

# print(set(a))

ans = 0
while len(set(a)) >= k:
    ans += 1
    a = [x // 2 for x in a]

print(ans)
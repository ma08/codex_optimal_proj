

n, m = map(int, input().split())
a_list = list(map(int, input().split()))

a_list.sort()

ans = 0
for i in range(m):
    if a_list[i] < 0:
        ans += -1 * a_list[i]

print(ans)

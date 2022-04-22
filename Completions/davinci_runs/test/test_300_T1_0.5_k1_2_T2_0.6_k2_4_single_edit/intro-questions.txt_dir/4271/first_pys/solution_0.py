

n = int(input())
dishes = list(map(int, input().split()))
points = list(map(int, input().split()))
bonus = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += points[dishes[i] - 1]
    if i > 0 and dishes[i] == dishes[i - 1] + 1:
        ans += bonus[dishes[i - 1] - 1]

print(ans)
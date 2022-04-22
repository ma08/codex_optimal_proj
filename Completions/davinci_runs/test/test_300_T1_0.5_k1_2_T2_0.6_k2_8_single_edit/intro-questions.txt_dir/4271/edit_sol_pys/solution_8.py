# cook your dish here

n = int(input())
dishes = list(map(int, input().split()))
points = [0] * n
bonus = [0] * n

for i in range(n):
    points[i] = int(input())

for i in range(n):
    bonus[i] = int(input())

ans = 0
for i in range(n):
    ans += points[dishes[i] - 1]
    if i > 0 and dishes[i] == dishes[i - 1] + 1:
        ans += bonus[dishes[i - 1] - 1]

print(ans)

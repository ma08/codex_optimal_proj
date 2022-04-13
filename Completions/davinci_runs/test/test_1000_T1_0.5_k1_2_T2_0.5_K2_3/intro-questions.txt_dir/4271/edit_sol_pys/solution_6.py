n = int(input())  # n = 3
dishes = list(map(int, input().split()))  # dishes = [1, 2, 3]
points = list(map(int, input().split()))  # points = [1, 2, 3]
bonus = list(map(int, input().split()))  # bonus = [0, 1, 2]

ans = 0
for i in range(n):
    ans += points[dishes[i] - 1]  # ans = 0 + 1
    if i > 0 and dishes[i] == dishes[i - 1] + 1:  # if 1 > 0 and dishes[1] == dishes[0] + 1
        ans += bonus[dishes[i - 1] - 1]  # ans = 1 + 0

print(ans)

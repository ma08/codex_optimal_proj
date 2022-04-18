n = int(input())  # number of dishes
dishes = list(map(int, input().split()))  # list of dishes
points = list(map(int, input().split()))  # points for each dish
bonus = list(map(int, input().split()))  # bonus points for each dish

ans = 0
for i in range(n):
    ans += points[dishes[i] - 1]
    if i > 0 and dishes[i] == dishes[i - 1] + 1:
        ans += bonus[dishes[i - 1] - 1]

print(ans)

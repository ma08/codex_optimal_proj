

n = int(input())  # n = 5

ans = 0  # ans = 0
for a in range(1, n + 1):  # a = 1, 2, 3, 4, 5
    for b in range(1, n + 1):  # b = 1, 2, 3, 4, 5
        c = n - a * b  # c = 5, 3, 2, 2, 1
        if c > 0:  # c > 0
            ans += 1  # ans = 1, 2, 3, 4, 5

print(ans)  # ans = 15


# -----Solution-----

n = int(input())
soft = 0
hard = 0

for i in range(n):
    cheese = input().split()
    if cheese[1] == "soft":
        soft += 1
    else:
        hard += 1

print(min(soft, hard))

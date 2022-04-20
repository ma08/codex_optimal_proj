
#-----Solution-----

n = int(input())
soft = 0
hard = 0

for i in range(n):
    cheese = input().split()[1]
    if cheese == "soft":
        soft += 1
    else:
        hard += 1

print(min(soft, hard))

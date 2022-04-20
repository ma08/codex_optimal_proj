

# SOLUTION

n = int(input())
soft = []
hard = []
for _ in range(n):
    cheese, ch = input().split()
    if ch == "soft":
        soft.append(cheese)
    else:
        hard.append(cheese)
print(len(soft))
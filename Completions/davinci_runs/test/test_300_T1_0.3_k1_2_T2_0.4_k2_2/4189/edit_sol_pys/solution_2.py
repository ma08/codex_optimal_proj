

n = int(input())
soft = hard = 0

for i in range(n):
    cheese = input().split()[1]
    soft += cheese == "soft"
    hard += cheese == "hard"

print(min(soft, hard))


# Get input
n = int(input())
a = [int(x) for x in input().split()]

# Get the largest number of days he can train
days = 0
for i in a:
    if i > days:
        days += 1

print(days)

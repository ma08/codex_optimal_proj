

# Get input
n = int(raw_input())
a = [int(x) for x in raw_input().split()]

# Get the largest number of days he can train for
days = 0
for i in range(n):
    if a[i] > days:
        days += 1

print(days)

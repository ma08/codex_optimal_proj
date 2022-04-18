

# Get input
n = int(input())
a = [int(i) for i in input().split()]

# Get the largest number of days he can train
days = 0
for i in range(n):
    if a[i] > days:
        days += 1

print(days)

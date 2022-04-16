
# Get input
n = int(input())
a = [int(x) for x in input().split()]

# Get the largest number of days he can train
days = 0
for i in range(n-1):
    if a[i] > days:
        days += 1

print(days)

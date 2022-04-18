
# Get input
n = int(input())
a = [int(x) for x in input().split()] # this is a list comprehension

# Get the largest number of days he can train
days = 0
for i in range(n):
    if a[i] > days:
        days += 1

print(days)

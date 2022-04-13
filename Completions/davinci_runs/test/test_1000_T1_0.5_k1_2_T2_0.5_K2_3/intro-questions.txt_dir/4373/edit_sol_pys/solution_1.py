
# Get input
n = int(input())
a = [int(x) for x in input().split()] # split the input into an array

# Get the largest number of days he can train in a row
days = 0
for i in range(n):
    if a[i] > days: # if the number at index i is greater than the number of days
        days += 1

print(days)

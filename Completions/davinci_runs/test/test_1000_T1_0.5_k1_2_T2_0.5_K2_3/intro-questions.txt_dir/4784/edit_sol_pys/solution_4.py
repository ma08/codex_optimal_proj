X = int(input())
n = int(input())

total_used = 0
for i in range(n):
    used = int(input())
    total_used += used

print(X + total_used)

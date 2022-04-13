

n = int(input())
a = [int(x) for x in input().split()]

days = 0
for i in range(n):
    if a[i] > days:
        days += 1

print(days)

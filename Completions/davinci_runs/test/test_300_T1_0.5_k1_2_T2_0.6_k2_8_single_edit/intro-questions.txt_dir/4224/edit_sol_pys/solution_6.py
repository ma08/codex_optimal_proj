

n = int(input())
a = [int(x) for x in input().split(',')]
b = [int(x) for x in input().split(',')]

count_a = 0
count_b = 0

for i in range(n):
    if (a[i] > b[i]):
        count_a += 1
    elif (a[i] < b[i]):
        count_b += 1

print(count_a, count_b)

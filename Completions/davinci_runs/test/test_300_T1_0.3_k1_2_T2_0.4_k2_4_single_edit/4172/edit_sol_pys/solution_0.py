

n = int(input())
a = [int(x) for x in input().split()][:n]

min_a = a[0]
max_a = a[0]

for i in a:
    if i > max_a:
        max_a = i
    if i < min_a:
        min_a = i

print(max_a - min_a)



n = int(input())
x = [int(i) for i in input().split()]

#print(n, x)

min_count = 0
max_count = 0

# min
curr = x[0]
min_count = 1
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        min_count += 1

# max
curr = x[0]
max_count = 1
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        max_count += 1
    elif x[i] == curr and i == len(x) - 1:
        max_count += 1

print(min_count, max_count)

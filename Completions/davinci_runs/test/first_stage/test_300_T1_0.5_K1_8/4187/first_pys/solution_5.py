

n = int(input())
a = [int(x) for x in input().split()]

max_length = 0
length = 0

for i in range(n):
    if a[i] == 0:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0

max_length = max(max_length, length)

print(max_length)
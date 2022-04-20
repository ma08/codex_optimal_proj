

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(abs(a[0] - a[1]))
    exit()

# The answer is the sum of the differences between the
# number of students with a certain skill level and the
# number of students with the skill level + 1

# We can just sort the list, and then iterate through it
# to find the differences

a.sort()

total = 0
for i in range(0, n, 2):
    total += a[i + 1] - a[i]

print(total)
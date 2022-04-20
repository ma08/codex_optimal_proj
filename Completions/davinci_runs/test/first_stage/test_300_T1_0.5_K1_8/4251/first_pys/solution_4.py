

# SOLUTION
# The problem is to find the minimum distance between two adjacent numbers in the sorted array of the matrix.
# The answer is the difference between the minimum and the second minimum number in the array.

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

# print(n, m)
# print(a)

b = []
for i in range(n):
    for j in range(m):
        b.append(a[i][j])

# print(b)
b.sort()
# print(b)

s = set()
for i in range(len(b) - 1):
    s.add(b[i + 1] - b[i])

# print(s)

if len(s) == 1:
    print(0)
else:
    print(min(s))
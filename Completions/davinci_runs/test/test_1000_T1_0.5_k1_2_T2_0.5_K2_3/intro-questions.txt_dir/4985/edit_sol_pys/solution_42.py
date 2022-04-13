
# input
n, m = map(int, input().split())

# initialize variables
c = []
for i in range(n):
    c.append(input())

# loop to find the shortest string
s = c[0]
for i in range(1, n):
    if len(c[i]) < len(s):
        s = c[i]

# print
print(s)

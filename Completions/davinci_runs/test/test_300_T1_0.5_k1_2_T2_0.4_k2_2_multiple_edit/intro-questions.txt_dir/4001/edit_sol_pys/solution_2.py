
# read n
n = int(input())
# read list of numbers
l = list(map(int, input().split()))

# create dictionary of numbers
d = {}
for i in l:
    d[i] = d.get(i, 0) + 1

# create list of odd numbers
x = []
for i in d:
    if d[i] % 2:
        x.append(i)

# print numbers
print(x[0], x[1])

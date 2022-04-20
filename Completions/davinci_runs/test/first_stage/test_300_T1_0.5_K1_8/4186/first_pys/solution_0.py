

input_line = input().split(" ")
n = int(input_line[0])
a = input_line[1:]

# a = [int(i) for i in a]

a.sort()

print(a)

d = {}

for i in range(0,n,2):
    if a[i] in d:
        d[a[i]] += 1
    else:
        d[a[i]] = 1

print(d)

count = 0
for k, v in d.items():
    if v % 2 == 0:
        count += v // 2
    else:
        count += v // 2
        count += 1

print(count)
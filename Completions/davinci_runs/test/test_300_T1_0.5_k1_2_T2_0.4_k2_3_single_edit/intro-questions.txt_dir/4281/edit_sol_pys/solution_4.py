
n = int(input())
x = [int(i) for i in input().split()]

#print(n, x)

min_cnt = 0
max_cnt = 0

# min
curr = x[0]
min_cnt = 1
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        min_cnt += 1

# max
curr = x[0]
max_cnt = 1
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        max_cnt += 1
    elif x[i] == curr and i == len(x)-1:
        max_cnt += 1

print(min_cnt, max_cnt)

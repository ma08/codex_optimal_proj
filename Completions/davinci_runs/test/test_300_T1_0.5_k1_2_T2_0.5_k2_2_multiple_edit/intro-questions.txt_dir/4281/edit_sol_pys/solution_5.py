

n = int(input())
x = [int(i) for i in input().split()]

# print(x)

min_cnt = 1
max_cnt = 1

# min
curr = x[0]
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        min_cnt += 1

# max
curr = x[0]
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        max_cnt += 1
    elif x[i] == curr and i == len(x)-1:
        max_cnt += 1

print(min_cnt, max_cnt)

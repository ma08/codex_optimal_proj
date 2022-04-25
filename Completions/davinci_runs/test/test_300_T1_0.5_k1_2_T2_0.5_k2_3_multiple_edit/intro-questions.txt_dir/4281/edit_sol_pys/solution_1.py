
n = int(input())
x = [int(i) for i in input().split()]

# min_cnt
curr = x[0] # x[0] is a color
min_cnt = 1
    # if the current color is different from the previous one,
    # change the current color and increase the counter
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        min_cnt += 1

# max_cnt
curr = x[0] # x[0] is a color
max_cnt = 1
for i in range(1, len(x)):
    # if the current color is different from the previous one,
    # change the current color and increase the counter
    if x[i] != curr:
        curr = x[i]
        max_cnt += 1
    # if the current color is the same as the previous one and
    # it is the last color in the list, increase the counter
    elif x[i] == curr and i == len(x)-1:
        max_cnt += 1

print(min_cnt, max_cnt)

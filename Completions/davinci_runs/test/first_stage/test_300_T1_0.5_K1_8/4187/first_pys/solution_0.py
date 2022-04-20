

n = int(input())
a = list(map(int, input().split()))

max_rest = 0

curr_rest = 0
for i in range(n):
    if a[i] == 1:
        curr_rest += 1
    else:
        curr_rest = 0
    max_rest = max(max_rest, curr_rest)

curr_rest = 0
for i in range(n):
    if a[i] == 1:
        curr_rest += 1
    else:
        curr_rest = 0
    max_rest = max(max_rest, curr_rest)

print(max_rest)
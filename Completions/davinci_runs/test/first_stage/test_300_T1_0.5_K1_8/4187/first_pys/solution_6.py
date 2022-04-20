

n = int(input())
a = list(map(int, input().split()))

max_rest = 0
rest_count = 0
for i in range(len(a)):
    if a[i] == 1:
        rest_count += 1
        max_rest = max(max_rest, rest_count)
    else:
        rest_count = 0

if max_rest == 0:
    print(0)
else:
    print(max_rest)
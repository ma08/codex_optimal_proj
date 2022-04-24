n = int(input())
a = list(map(int, input().split()))

max_count = 0
count = 0

for i in a:
    if i == 0:
        max_count = max(max_count, count)
        count = 0
    else:
        count += 1

max_count = max(max_count, count)
print(max_count)

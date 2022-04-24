

n = int(input())
a = list(map(int, input().split()))

max_len = 0
length = 0

for i in a:
    if i == 0:
        max_len = max(max_len, length)
        length = 0
    else:
        length += 1

max_len = max(max_len, length)
print(max_len)


n = int(input())
a = list(map(int, input().split()))

max_len = 0
len = 0

for i in a:
    if i == 0:
        max_len = max(max_len, len)
        len = 0
    else:
        len += 1

max_len = max(max_len, len)
print(max_len)


n = int(input())
a = list(map(int, input().split()))

max_length = 0
length = 0

for i in a:
    if i == 0:
        max_length = max(max_length, length)
        length = 0
    else:
        length += 1

max_length = max(max_length, length)
print(max_length)

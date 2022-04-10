n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(2)
    exit()

max_length = 2
length = 2
for i in range(1, n - 1):
    if a[i - 1] < a[i] <= a[i + 1]:
        length += 1
    else:
        length = 2
    if length > max_length:
        max_length = length

print(max_length)



n = int(input())
array = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if array[i - 1] < array[i] < array[i + 1] or array[i + 1] < array[i] < array[i - 1]:
        count += 1

print(count)
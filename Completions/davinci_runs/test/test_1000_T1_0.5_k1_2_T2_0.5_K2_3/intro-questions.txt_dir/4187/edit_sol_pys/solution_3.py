
n = int(input())
a = list(map(int, input().split()))
max_consecutive = 0
consecutive = 0

for i in a:
    if i == 0:
        max_consecutive = max(max_consecutive, consecutive)
        consecutive = 0
    else:
        consecutive += 1

max_consecutive = max(max_consecutive, consecutive)
print(max_consecutive)

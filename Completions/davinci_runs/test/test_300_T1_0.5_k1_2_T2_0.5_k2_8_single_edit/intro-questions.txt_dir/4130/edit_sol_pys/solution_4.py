

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
count = 1
for i in range(0, n):
    if i == 0:
        count += 1

print(count)

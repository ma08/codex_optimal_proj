
n, k = map(int, input().split())
problems = list(map(int, input().split()))

count = 0
while True:
    if problems[0] > k and problems[-1] > k:
        break
    if problems[0] <= k:
        count += 1
        problems.pop(0)
    if problems[-1] <= k:
        count += 1
        problems.pop()
print(count)

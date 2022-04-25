
n = int(input())
a = list(map(int, input().split()))

max_res = 0
res = 0

for i in a:
    if i == 0:
        max_res = max(max_res, res)
        res = 0
    else:
        res += 1

max_res = max(max_res, res)
print(max_res)

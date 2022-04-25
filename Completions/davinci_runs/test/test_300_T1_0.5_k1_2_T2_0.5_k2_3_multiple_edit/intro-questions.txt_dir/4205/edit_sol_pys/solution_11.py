

n = int(input())
p = list(map(int, input().split()))

sorted_p = sorted(p)

diff_index = []

for i in range(n):
    if p[i] != sorted_p[i]:
        diff_index.append(i)

if len(diff_index) > 2:
    print('NO')
else:
    print('YES')

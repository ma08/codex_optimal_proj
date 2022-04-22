

n, m = map(int, input().split())
xy_list = [list(map(int, input().split())) for _ in range(n)]

xy_list.sort(key=lambda x: x[0])

for i in range(n):
    if xy_list[i][0] >= xy_list[i][1]:
        print('War')
        exit()

print('No War')

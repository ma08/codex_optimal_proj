'''
    https://www.hackerrank.com/challenges/angry-professor
'''

for i in range(int(input())):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    count = 0
    for time in times:
        if time <= 0:
            count += 1

    if count >= k:
        print('NO')
    else:
        print('YES')



n, T = map(int, input().split())
tasks = list(map(int, input().split()))
count = 0
time = 0
for i in range(n):
    if time + tasks[i] <= T:
        count += 1
        time += tasks[i]
    else:
        break

print(count)

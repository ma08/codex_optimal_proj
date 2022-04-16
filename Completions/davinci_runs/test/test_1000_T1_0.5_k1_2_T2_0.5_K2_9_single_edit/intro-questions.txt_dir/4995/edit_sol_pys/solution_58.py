

n = int(input())

sum_time = 0
sum_minutes = 0
for i in range(n):
    m, s = map(int, input().split())
    sum_time += s
    sum_minutes += m

if sum_minutes == 0:
    print("measurement error")
else:
    print(sum_time/sum_minutes)


N = int(input())

total_time = 0
total_minutes = 0
for i in range(N):
    M, S = map(int, input().split())
    total_time += S
    total_minutes += M

if total_minutes == 0:
    print("measurement error")
else:
    print(total_time/total_minutes)

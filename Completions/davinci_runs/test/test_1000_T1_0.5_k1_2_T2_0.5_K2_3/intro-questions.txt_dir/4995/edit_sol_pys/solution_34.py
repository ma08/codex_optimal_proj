
n = int(input())

minutes = 0.0
seconds = 0.0

for _ in range(n):
    m, s = map(int, input().split())
    minutes += m
    seconds += s

if seconds/minutes > 60:
    print("measurement error")
else:
    print(round(seconds/minutes, 1))

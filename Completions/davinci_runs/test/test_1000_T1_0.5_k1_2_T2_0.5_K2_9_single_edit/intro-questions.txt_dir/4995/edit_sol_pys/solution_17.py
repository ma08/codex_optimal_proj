

n = int(input())

minutes = 0.0
seconds = 0.0

for i in range(n):
    m, s = map(int, input().split())
    minutes += m
    seconds += s

if seconds/minutes > 59:
    print("measurement error")
else:
    print(seconds/minutes)

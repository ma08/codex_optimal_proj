

n = int(input()) # number of students

minutes = 0
score = 0
seconds = 0

for i in range(n):
    m, s, p = map(int, input().split())
    minutes += m
    score += p
    seconds += s

if minutes == 0 or seconds/minutes > 60:
    print("measurement error")
else:
    print(score/minutes)

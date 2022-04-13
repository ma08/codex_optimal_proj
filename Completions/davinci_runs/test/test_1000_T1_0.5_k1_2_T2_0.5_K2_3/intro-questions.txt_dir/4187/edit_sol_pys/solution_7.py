
n = int(input())
a = list(map(int, input().split()))

max_streak = 0
streak = 0

for i in a:
    if i == 0:
        max_streak = max(max_streak, streak)
        streak = 0
    else:
        streak += 1

max_streak = max(max_streak, streak)
print(max_streak)

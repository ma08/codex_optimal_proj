
d, t, s = map(int, input().split())  # distance, time, speed

if d / s <= t:
    print("Yes")
else:
    print("No")

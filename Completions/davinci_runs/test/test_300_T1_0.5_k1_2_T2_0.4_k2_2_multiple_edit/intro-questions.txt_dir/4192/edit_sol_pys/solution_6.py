
d, t, s = map(int, input().split())  # d = distance, t = time, s = speed

if d / s <= t:
    print("Yes")
else:
    print("No")

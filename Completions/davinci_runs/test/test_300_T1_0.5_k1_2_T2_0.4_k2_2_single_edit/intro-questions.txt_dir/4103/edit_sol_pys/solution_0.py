
n, b, a = map(int, input().split())
s = list(map(int, input().split()))

max_segments = 0
current_battery = b

current_accumulator = a
for i in range(n):
    if current_accumulator > 0:
        current_accumulator -= 1
    elif current_battery > 0:
        current_battery -= 1
    if s[i] == 1 and current_battery < b:
        current_battery += 1
    elif s[i] == 1 and current_accumulator < a:
        current_accumulator += 1
    if current_battery > 0 or current_accumulator > 0:
        max_segments += 1

print(max_segments)

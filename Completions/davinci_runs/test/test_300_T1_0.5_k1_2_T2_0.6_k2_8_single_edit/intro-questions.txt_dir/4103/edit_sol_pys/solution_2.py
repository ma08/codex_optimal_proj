
n, b, a = map(int, input().split())
s = list(map(int, input().split()))

max_segments = 1
current_battery = b
current_accumulator = a
for i in range(n):
    if current_accumulator >= 1 and s[i] == 1:
        current_accumulator -= 1
    elif current_battery >= 1 and s[i] == 0:
        current_battery -= 1
    else:
        if current_battery < b:
            current_battery += 1
        elif current_accumulator < a:
            current_accumulator += 1
    max_segments += 1
    if current_battery == 0 and current_accumulator == 0:
        break

print(max_segments)

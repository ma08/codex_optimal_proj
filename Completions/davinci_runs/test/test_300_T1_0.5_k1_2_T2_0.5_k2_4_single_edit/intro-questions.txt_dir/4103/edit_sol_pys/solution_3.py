n, b, a = map(int, input().split())
s = list(map(int, input().split()))


a_limit = a
b_limit = b

if a > b:
    a_limit = b
elif b > a:
    b_limit = a

max_segments = 0
current_battery = b_limit
current_accumulator = a_limit
for i in range(n):
    if current_accumulator >= 1:
        current_accumulator -= 1
    else:
        current_battery -= 1
    if s[i] == 1:
        if current_battery < b_limit:
            current_battery += 1
        else:
            current_accumulator += 1
    max_segments += 1
    if current_battery == 0 and current_accumulator == 0:
        break

print(max_segments)



n, b, a = map(int, input().split())  # n - number of segments, b - battery, a - accumulator
s = list(map(int, input().split()))

max_segments = 0  # number of segments that can be passed
current_battery = b
current_accumulator = a
for i in range(n):
    if current_accumulator >= 1:  # check if accumulator is not empty
        current_accumulator -= 1
    else:  # if accumulator is empty
        current_battery -= 1
    if s[i] == 1:  # check if segment is sunny
        if current_battery < b:  # if battery is not full
            current_battery += 1
        else:  # if battery is full
            current_accumulator += 1
    max_segments += 1  # add 1 to max_segments
    if current_battery == 0 and current_accumulator == 0:
        break

print(max_segments)

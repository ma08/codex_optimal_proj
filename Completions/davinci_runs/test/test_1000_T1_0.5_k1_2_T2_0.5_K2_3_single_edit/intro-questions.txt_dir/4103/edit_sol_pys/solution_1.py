

n, b, a = map(int, input().split())  # number of segments, battery capacity, accumulator capacity
s = list(map(int, input().split()))

max_segments = 0  # number of segments where we can go
current_battery = b  # current battery level
current_accumulator = a  # current accumulator level

for i in range(n):
    if current_accumulator >= 1:  # if we can use accumulator
        current_accumulator -= 1  # use accumulator
    else:
        current_battery -= 1  # otherwise use battery
    if s[i] == 1:  # if we can charge our accumulator
        if current_battery < b:  # if battery is not full
            current_battery += 1  # charge battery
        else:
            current_accumulator += 1  # otherwise charge accumulator
    max_segments += 1  # go to next segment
    if current_battery == 0 and current_accumulator == 0:  # if we have no energy
        break

print(max_segments)

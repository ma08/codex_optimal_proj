

n, b, a = map(int, input().split())  # number of segments, battery, accumulator
s = list(map(int, input().split()))  # segments

max_segments = 0  # maximum number of segments
current_battery = b  # current battery
current_accumulator = a  # current accumulator
for i in range(n):  # iterate over segments
    if current_accumulator >= 1:  # if accumulator is not empty
        current_accumulator -= 1  # use accumulator
    else:  # if accumulator is empty
        current_battery -= 1  # use battery
    if s[i] == 1:  # if segment is dangerous
        if current_battery < b:  # if battery is not full
            current_battery += 1  # charge battery
        else:  # if battery is full
            current_accumulator += 1  # charge accumulator
    max_segments += 1  # increase number of segments
    if current_battery == 0 and current_accumulator == 0:  # if both battery and accumulator are empty
        break  # stop

print(max_segments)  # print maximum number of segments

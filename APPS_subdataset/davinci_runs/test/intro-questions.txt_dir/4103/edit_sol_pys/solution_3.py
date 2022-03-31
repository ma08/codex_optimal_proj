

n, b, a = map(int, input().split())  # n - number of segments, b - battery capacity, a - accumulator capacity
s = list(map(int, input().split()))  # s - list of segments

battery = b  # current battery capacity
accumulator = a  # current accumulator capacity

segments = 0  # number of segments passed

for i in range(n):
    if s[i] == 1:  # if segment is sunny
        if battery < b:  # if battery is not full
            battery += 1
        else:  # if battery is full
            accumulator += 1
    if battery > 0:  # if battery is not empty
        battery -= 1
        segments += 1
    elif accumulator > 0:  # if accumulator is not empty
        accumulator -= 1
        segments += 1
    else:  # if both battery and accumulator are empty
        break

print(segments)

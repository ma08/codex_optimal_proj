

# SOLUTION
# The solution is to use the accumulator when it is possible and use the battery when the accumulator is empty. The accumulator is used when the current segment is exposed to sunlight and the accumulator is not empty. The battery is used when the accumulator is empty and the battery is not empty. The accumulator is recharged when the current segment is exposed to sunlight and the accumulator is empty. The accumulator is recharged when the battery is used and the current segment is exposed to sunlight.

n, b, a = map(int, input().split())
s = list(map(int, input().split()))

# Initialize the accumulator and the battery.
accumulator = a
battery = b

# Initialize the number of segments passed.
segments_passed = 0

# Go through all the segments.
for i in range(n):
    # If the accumulator is not empty and the current segment is exposed to sunlight, use the accumulator.
    if accumulator > 0 and s[i] == 1:
        accumulator -= 1
        segments_passed += 1
    # If the accumulator is empty and the battery is not empty, use the battery.
    elif accumulator == 0 and battery > 0:
        battery -= 1
        segments_passed += 1
    # If the accumulator is empty and the battery is empty, stop
    elif accumulator == 0 and battery == 0:
        break
    # If the accumulator is not empty and the current segment is not exposed to sunlight, use the accumulator
    elif accumulator > 0 and s[i] == 0:
        accumulator -= 1
        segments_passed += 1
    # If the accumulator is empty and the battery is not empty and the current segment is exposed to sunlight, recharge the accumulator
    elif accumulator == 0 and battery > 0 and s[i] == 1:
        accumulator += 1
        battery -= 1
        segments_passed += 1

# Print the number of segments passed
print(segments_passed)

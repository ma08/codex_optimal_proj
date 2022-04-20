

# SOLUTION 1
# The solution is to use the accumulator when it is possible and use the battery when the accumulator is empty. The accumulator is used when the current segment is exposed to sunlight and the accumulator is not empty. The battery is used when the accumulator is empty and the battery is not empty. The accumulator is recharged when the current segment is exposed to sunlight and the accumulator is empty. The accumulator is recharged when the battery is used and the current segment is exposed to sunlight.

n, b, a = map(int, input().split()) # Read the input
s = list(map(int, input().split())) # Read the input

# Initialize the accumulator and the battery
accumulator = a # Initialize the accumulator
battery = b # Initialize the battery

# Initialize the number of segments passed
segments_passed = 0 # Initialize the number of segments passed

# Go through all the segments
for i in range(n):
    if accumulator > 0 and s[i] == 1: # If the accumulator is not empty and the current segment is exposed to sunlight, use the accumulator
        accumulator -= 1 # Use the accumulator
        segments_passed += 1 # Update the number of segments passed
    elif accumulator == 0 and battery > 0: # If the accumulator is empty and the battery is not empty, use the battery
        battery -= 1 # Use the battery
        segments_passed += 1 # Update the number of segments passed
    elif accumulator == 0 and battery == 0: # If the accumulator is empty and the battery is empty, stop
        break # Stop
    elif accumulator > 0 and s[i] == 0: # If the accumulator is not empty and the current segment is not exposed to sunlight, use the accumulator
        accumulator -= 1 # Use the accumulator
        segments_passed += 1 # Update the number of segments passed
    elif accumulator == 0 and battery > 0 and s[i] == 1: # If the accumulator is empty and the battery is not empty and the current segment is exposed to sunlight, recharge the accumulator
        accumulator += 1 # Recharge the accumulator
        battery -= 1 # Use the battery
        segments_passed += 1 # Update the number of segments passed

# Print the number of segments passed
print(segments_passed) # Print the number of segments passed



def solve(n, b, a, s):
    # initialize variables for the accumulator and the battery
    a_charge = 0
    b_charge = 0
    # initialize variables for the max distance and the current segment
    max_dist = 1
    current_segment = 0
    # loop through all segments
    for segment in s:
        # if the current segment is exposed to sunlight
        # and the accumulator is not full
        if segment == 1 and a_charge < a:
            # increase the charge on the accumulator
            a_charge += 1
        # if the current segment is not exposed to sunlight
        # and the accumulator is not empty
        elif segment == 0 and a_charge > 0:
            # decrease the charge on the accumulator
            a_charge -= 1
        # if the current segment is not exposed to sunlight
        # and the battery is not full
        elif segment == 0 and b_charge < b:
            # increase the charge on the battery
            b_charge += 1
        # if the current segment is exposed to sunlight
        # and the battery is not empty
        elif segment == 1 and b_charge > 0:
            # decrease the charge on the battery
            b_charge -= 1
        # if the current segment is not exposed to sunlight
        # and the battery and the accumulator are both empty
        elif segment == 0 and a_charge == 0 and b_charge == 0:
            # break the loop
            break
        # if the current segment is exposed to sunlight
        # and the battery and the accumulator are both full
        elif segment == 1 and a_charge == a and b_charge == b:
            # break the loop
            break
        # update the current segment
        current_segment += 1
        # if the current segment is the last segment
        # the robot can move forward
        if current_segment == n - 1:
            # increase the max distance
            max_dist += 1
    # return the max distance
    return max_dist 

n, b, a = map(int, input().split())
s = list(map(int, input().split()))
print(solve(n, b, a, s))

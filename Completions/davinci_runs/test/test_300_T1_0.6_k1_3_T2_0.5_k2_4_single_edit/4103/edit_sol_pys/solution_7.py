

def solve(n, b, a, s, i = 0, b_charge = 0, a_charge = 0, max_dist = 0):
    # initialize variables
    b_charge = b_charge + b
    a_charge = a_charge + a
    while i < n:
        # if there is no charge on the accumulator
        # and the current segment is exposed to sunlight
        # charge the accumulator
        if a_charge == 0 and s[i] == 1:
            a_charge += 1
            i += 1
        # if there is no charge on the battery
        # and the current segment is not exposed to sunlight
        # charge the battery
        elif b_charge == 0 and s[i] == 0:
            b_charge += 1
            i += 1
        # if there is charge on the accumulator
        # and the current segment is not exposed to sunlight
        # use the accumulator
        elif a_charge != 0 and s[i] == 0:
            a_charge -= 1
            i += 1
        # if there is charge on the battery
        # and the current segment is exposed to sunlight
        # use the battery
        elif b_charge != 0 and s[i] == 1:
            b_charge -= 1
            i += 1
        # if the battery and accumulator are both full
        # and no charge can be gained
        # the robot can't move forward
        else:
            break
        # increase the max distance
        max_dist += 1
    return max_dist

n, b, a = map(int, input().split()) # number of segments, battery capacity, accumulator capacity
s = list(map(int, input().split()))
print(solve(n, b, a, s))

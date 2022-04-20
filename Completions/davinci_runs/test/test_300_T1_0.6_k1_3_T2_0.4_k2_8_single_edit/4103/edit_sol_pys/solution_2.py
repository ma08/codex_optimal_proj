

def solve(n, b, a, s, m):
    # initialize variables
    i = 0
    b_charge = b
    a_charge = a
    max_dist = m
    while i < n:
        # if there is no charge on the battery
        # and the current segment is not exposed to sunlight
        # charge the battery
        if b_charge == 0 and s[i] == 0:
            b_charge += 1
            i += 1
        # if there is no charge on the accumulator
        # and the current segment is exposed to sunlight
        # charge the accumulator
        elif a_charge == 0 and s[i] == 1:
            a_charge += 1
            i += 1
        # if there is charge on the accumulator
        # and the current segment is exposed to sunlight
        # use the accumulator
        elif a_charge > 0 and s[i] == 1:
            a_charge -= 1
            i += 1
        # if there is charge on the battery
        # and the current segment is not exposed to sunlight
        # use the battery
        elif b_charge > 0 and s[i] == 0:
            b_charge -= 1
            i += 1
        # if the battery is empty
        # and the accumulator is empty
        # and the current segment is not exposed to sunlight
        # the robot can't move forward
        elif b_charge == 0 and a_charge == 0 and s[i] == 0:
            break
        # if the battery is empty
        # and the accumulator is empty
        # and the current segment is exposed to sunlight
        # the robot can't move forward
        elif b_charge == 0 and a_charge == 0 and s[i] == 1:
            break
        # if the battery is full
        # and the accumulator is full
        # and the current segment is not exposed to sunlight
        # the robot can't move forward
        elif b_charge == b and a_charge == a and s[i] == 0:
            break
        # if the battery is full
        # and the accumulator is full
        # and the current segment is exposed to sunlight
        # the robot can't move forward
        elif b_charge == b and a_charge == a and s[i] == 1:
            break
        # if the battery is full
        # and the accumulator is empty
        # and the current segment is not exposed to sunlight
        # the robot can't move forward
        elif b_charge == b and a_charge == 0 and s[i] == 0:
            break
        # if the battery is full
        # and the accumulator is empty
        # and the current segment is exposed to sunlight
        # the robot can't move forward
        elif b_charge == b and a_charge == 0 and s[i] == 1:
            break
        # if the battery is empty
        # and the accumulator is full
        # and the current segment is not exposed to sunlight
        # the robot can't move forward
        elif b_charge == 0 and a_charge == a and s[i] == 0:
            break
        # if the battery is empty
        # and the accumulator is full
        # and the current segment is exposed to sunlight
        # the robot can't move forward
        elif b_charge == 0 and a_charge == a and s[i] == 1:
            break
        # if the battery is full
        # and the accumulator is not empty
        # and the current segment is not exposed to sunlight
        # the robot can't move forward
        elif b_charge == b and a_charge > 0 and s[i] == 0:
            break
        # if the battery is full
        # and the accumulator is not empty
        # and the current segment is exposed to sunlight
        # the robot can't move forward
        elif b_charge == b and a_charge > 0 and s[i] == 1:
            break
        # if the battery is not empty
        # and the accumulator is full
        # and the current segment is not exposed to sunlight
        # the robot can't move forward
        elif b_charge > 0 and a_charge == a and s[i] == 0:
            break
        # if the battery is not empty
        # and the accumulator is full
        # and the current segment is exposed to sunlight
        # the robot can't move forward
        elif b_charge > 0 and a_charge == a and s[i] == 1:
            break
        # if the battery is empty
        # and the accumulator is not empty
        # and the current segment is not exposed to sunlight
        # the robot can't move forward
        elif b_charge == 0 and a_charge > 0 and s[i] == 0:
            break
        # if the battery is empty
        # and the accumulator is not empty
        # and the current segment is exposed to sunlight
        # the robot can't move forward
        elif b_charge == 0 and a_charge > 0 and s[i] == 1:
            break
        # if the battery is not empty
        # and the accumulator is empty
        # and the current segment is not exposed to sunlight
        # the robot can't move forward
        elif b_charge > 0 and a_charge == 0 and s[i] == 0:
            break
        # if the battery is not empty
        # and the accumulator is empty
        # and the current segment is exposed to sunlight
        # the robot can't move forward
        elif b_charge > 0 and a_charge == 0 and s[i] == 1:
            break
        else:
            break
        # increase the max distance
        max_dist += 1
    return max_dist

n, b, a = map(int, input().split())
s = list(map(int, input().split()))
m = 0
print(solve(n, b, a, s, m))

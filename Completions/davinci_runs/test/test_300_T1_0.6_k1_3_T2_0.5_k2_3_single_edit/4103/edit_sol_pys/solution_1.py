

def solve(n, b, a, s, i=0, b_charge=0, a_charge=0, max_dist=0):
    # initialize variables
    while i < n:
        # if there is no charge on the accumulator
        # and the current segment is exposed to sunlight
        # charge the accumulator
        if a_charge < a and s[i] == 1:
            a_charge += 1
            i += 1
        # if there is no charge on the battery
        # and the current segment is not exposed to sunlight
        # charge the battery
        elif b_charge < b and s[i] == 0:
            b_charge += 1
            i += 1
        # if there is charge on the accumulator
        # and the current segment is not exposed to sunlight
        # use the accumulator
        elif a_charge > 0 and s[i] == 1:
            a_charge -= 1
            i += 1
        # if there is charge on the battery
        # and the current segment is exposed to sunlight
        # use the battery
        elif b_charge > 0 and s[i] == 0:
            b_charge -= 1
            i += 1
        # the robot can't move forward
        else:
            # if the battery and accumulator are both full
            # and no charge can be gained
            if a_charge == a and b_charge == b and s[i] == 0:
                break
            # if the robot is exposed to sunlight
            # and there is no charge on the accumulator
            elif s[i] == 1 and a_charge == 0:
                break
            # if the robot is not exposed to sunlight
            # and there is no charge on the battery
            elif s[i] == 0 and b_charge == 0:
                break
        # increase the max distance
        max_dist += 1
    return max_dist, solve(n, b, a, s, i=i+1, b_charge=b_charge, a_charge=a_charge, max_dist=max_dist)

n, b, a = map(int, input().split())
s = list(map(int, input().split()))
print(max(solve(n, b, a, s)))

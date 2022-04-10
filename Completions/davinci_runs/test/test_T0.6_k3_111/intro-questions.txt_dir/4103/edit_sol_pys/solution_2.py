

# The main idea is to keep track of the maximum number of segments that can be passed with the battery and the accumulator
# The accumulator can only be used to pass segments that are exposed to sunlight
# The battery can only be used to pass segments that are not exposed to sunlight
# When using the battery, the accumulator is charged by one
# When using the accumulator, the battery is charged by one

n, b, a = map(int, input().split())  # n is number of segments, b is battery capacity, a is accumulator capacity
s = list(map(int, input().split()))  # s is a list of integers, 1 means exposed to sunlight, 0 means not exposed to sunlight

max_segments = 0  # maximum number of segments that can be passed
b_cur = b  # current battery capacity
a_cur = a  # current accumulator capacity

for i in range(n):
    if s[i] == 1:  # segment is exposed to sunlight
        if a_cur > 0:
            a_cur -= 1
            b_cur += 1
        elif b_cur > 0:
            b_cur -= 1
    else:  # segment is not exposed to sunlight
        if b_cur > 0:
            b_cur -= 1
            a_cur += 1
        elif a_cur > 0:
            a_cur -= 1
    if a_cur == 0 and b_cur == 0:  # if both accumulator and battery are empty, stop
        break
    max_segments += 1  # increment the maximum number of segments that can be passed
print(max_segments)

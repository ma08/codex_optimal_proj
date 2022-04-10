

# The main idea is to keep track of the maximum number of segments that can be passed with the battery and the accumulator
# The accumulator can only be used to pass segments that are exposed to sunlight
# The battery can only be used to pass segments that are not exposed to sunlight
# When using the battery, the accumulator is charged by one
# When using the accumulator, the battery is charged by one

n, b, a = map(int, input().split())
s = list(map(int, input().split()))

max_segments = 0
b_cur = b
a_cur = a

for i in range(n):
    if s[i] == 1:
        if a_cur > 0:
            a_cur -= 1
            b_cur += 1
        elif b_cur > 0:
            b_cur -= 1
    else:
        if b_cur > 0:
            b_cur -= 1
            a_cur += 1
        elif a_cur > 0:
            a_cur -= 1
    if a_cur == 0 and b_cur == 0:
        break
    max_segments += 1
print(max_segments)

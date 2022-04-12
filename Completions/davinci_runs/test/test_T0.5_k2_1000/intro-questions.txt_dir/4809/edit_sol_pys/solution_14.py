

def play_coconut_splat(s, n, k):  # s is the number of coconuts, n is the number of people, and k is the starting position
    if s % 2 == 0:  # if the number of coconuts is even
        return (s // 2) % n + k  # return the number of coconuts divided by 2, modulo the number of people, plus the starting position
    else:  # if the number of coconuts is odd
        return s // 2 % n + k  # return the number of coconuts divided by 2, modulo the number of people, plus the starting position

print(play_coconut_splat(int(input()), int(input()), int(input())))  # print the result of the function

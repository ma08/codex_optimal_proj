

def play_coconut_splat(s, n): # s is the number of coconuts, n is the number of people
    if s % 2 == 0: # if the number of coconuts is even
        return (s // 2 - 1) % n + 1 # then the person who survives is the one who receives the last coconut
    else:
        return (s // 2 - 1) % n + 1 # if the number of coconuts is odd then the person who survives is the one who receives the last coconut

print(play_coconut_splat(int(input()), int(input())))

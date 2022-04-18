

def play_coconuts_splat(s, n):
    s = s - 1
    return s % n + 1


print(play_coconuts_splat(int(input()), int(input())))

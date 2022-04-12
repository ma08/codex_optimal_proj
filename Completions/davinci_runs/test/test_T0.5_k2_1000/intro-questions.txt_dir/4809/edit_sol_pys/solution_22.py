

def play_coconut_splat(s, n, m):
    if s % 2 == 0:
        return ((s // 2) % n) + 1 + m
    else:
        return (s // 2) % n + 1 + m

print(play_coconut_splat(int(input()), int(input()), int(input())))

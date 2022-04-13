

def play_coconut_splat(s, n):
    return (s // 2) % n + 1 if s % 2 == 0 else (s // 2) % n + 1

print(play_coconut_splat(int(input()), int(input())))

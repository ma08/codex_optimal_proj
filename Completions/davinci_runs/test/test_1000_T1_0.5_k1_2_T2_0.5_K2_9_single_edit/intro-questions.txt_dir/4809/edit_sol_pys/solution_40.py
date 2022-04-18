

def play_coconut_splat(s, n):
    if s % 2 == 0:
        return (s // 2) % n
    else:
        return s // 2 % n

print(play_coconut_splat(int(input()), int(input())))

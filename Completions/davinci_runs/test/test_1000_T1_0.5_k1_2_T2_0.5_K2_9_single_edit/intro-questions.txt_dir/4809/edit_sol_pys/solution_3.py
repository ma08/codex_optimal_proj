

def play_coconut_splat(s, n):
    if s % 2 == 0:
        return s // 2 % n + 1
    else:
        return s // 2 % n + 1

print(play_coconut_splat(int(input()), int(input())))

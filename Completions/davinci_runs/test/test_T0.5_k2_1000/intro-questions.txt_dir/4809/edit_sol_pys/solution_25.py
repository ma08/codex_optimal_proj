
def play_coconut_splat(s, n, k):
    if s % 2 == 0:
        return (s // 2) % n + k - 1
    else:
        return s // 2 % n + k - 1

print(play_coconut_splat(int(input()), int(input()), int(input())))

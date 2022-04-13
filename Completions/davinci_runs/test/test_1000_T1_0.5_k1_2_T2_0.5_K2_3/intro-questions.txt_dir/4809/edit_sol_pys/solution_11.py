

import math
def play_coconut_splat(s, n):
    return math.ceil(s / 2) % n

print(play_coconut_splat(int(input()), int(input())))

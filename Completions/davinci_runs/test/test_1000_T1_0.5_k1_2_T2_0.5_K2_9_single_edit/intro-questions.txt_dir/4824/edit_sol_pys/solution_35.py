
import math

C, P = map(int, input().split())
heights = list(map(int, input().split()))

def get_count(h):
    if P == 1:
        return math.ceil(h / 2)
    elif P == 2:
        return math.ceil(h / 4)
    elif P == 3:
        return math.ceil(h / 4)
    elif P == 4:
        return math.ceil(h / 6)
    elif P == 5:
        return math.ceil(h / 10)
    elif P == 6:
        return math.ceil(h / 12)
    elif P == 7:
        return math.ceil(h / 16)

for h in heights:
    print(get_count(h))

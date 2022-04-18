

import math

def get_smaller_brick_count(height, small_bricks, big_bricks):
    height_small_bricks = height * (height + 1)
    height_big_bricks = height * 2
    if small_bricks >= height_small_bricks + big_bricks * 4:
        return 0, big_bricks
    return math.ceil((height_small_bricks - small_bricks) / 4), 0

if __name__ == "__main__":
    height, small_bricks, big_bricks = map(int, input().split())
    print(*get_smaller_brick_count(height, small_bricks, big_bricks))

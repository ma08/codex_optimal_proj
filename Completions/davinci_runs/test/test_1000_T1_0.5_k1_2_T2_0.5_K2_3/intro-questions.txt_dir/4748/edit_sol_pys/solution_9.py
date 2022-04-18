

import math

def get_smaller_brick_count(height, small_bricks, big_bricks, height_small_bricks, height_big_bricks):
    height_small_bricks = (2 * height - 1) * height
    height_big_bricks = 2 * height

    if small_bricks >= height_small_bricks:
        return 0, 0

    elif height_small_bricks >= big_bricks * 4:
        return height_small_bricks - big_bricks * 4, big_bricks
    else:
        return 0, math.ceil(height_small_bricks / 4)

if __name__ == "__main__":
    height, small_bricks, big_bricks = map(int, input().split())
    height_small_bricks = 0
    height_big_bricks = 0
    print(*get_smaller_brick_count(height, small_bricks, big_bricks, height_small_bricks, height_big_bricks))

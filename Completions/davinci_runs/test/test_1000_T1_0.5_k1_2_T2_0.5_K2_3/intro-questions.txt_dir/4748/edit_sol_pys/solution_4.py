

import math

def get_small_brick_count(height, small_bricks, big_bricks):
    height_small_bricks = (2 * height - 1) * height // 2
    height_big_bricks = height

    if height_small_bricks <= small_bricks:
        return 0, big_bricks

    height_small_bricks -= small_bricks 

    if height_small_bricks >= big_bricks * 2:
        return height_small_bricks - big_bricks * 2, big_bricks
    else:
        return 0, math.ceil(height_small_bricks / 2)

if __name__ == "__main__":
    height, small_bricks, big_bricks = map(int, input().split())
    print(*get_small_brick_count(height, small_bricks, big_bricks))

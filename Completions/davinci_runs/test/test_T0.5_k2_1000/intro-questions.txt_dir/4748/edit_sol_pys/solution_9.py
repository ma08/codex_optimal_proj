
import math

def get_smaller_brick_count(height, small_bricks, big_bricks, small_brick_height=1, big_brick_height=5):
    height_small_bricks = (2 * height - 1) * small_brick_height  # высота которую можно сделать из маленьких кирпичей
    height_big_bricks = 2 * height * big_brick_height  # высота которую можно сделать из больших кирпичей

    if small_bricks >= height_small_bricks:  # если маленьких кирпичей достаточно для постройки высоты
        return 0, 0

    height_small_bricks -= small_bricks  # высота которую не хватает маленьких кирпичей
    height_big_bricks -= big_bricks  # высота которую не хватает больших кирпичей

    if height_small_bricks >= big_bricks * big_brick_height:  # если больших кирпичей достаточно для постройки высоты
        return height_small_bricks - big_bricks * big_brick_height, big_bricks
    else:  # если больших кирпичей недостаточно для постройки высоты
        return 0, math.ceil(height_small_bricks / big_brick_height)

if __name__ == "__main__":
    height, small_bricks, big_bricks = map(int, input().split())
    print(*get_smaller_brick_count(height, small_bricks, big_bricks))

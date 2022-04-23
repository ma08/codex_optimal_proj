

import sys

def max_happiness(x):
    """
    Args:
        x (int): the amount of yen that Takahashi has
    Returns:
        int: the maximum number of happiness points that can be earned
    """
    return x // 500 * 1000 + x % 500 // 5 * 5 # 分母が500で割り切れる個数を求めて、その個数*1000を足していく。残りの分母が5で割り切れる個数を求めて、その個数*5を足していく

def main():
    x = int(sys.stdin.readline().rstrip())
    print(max_happiness(x))

if __name__ == '__main__':
    main()

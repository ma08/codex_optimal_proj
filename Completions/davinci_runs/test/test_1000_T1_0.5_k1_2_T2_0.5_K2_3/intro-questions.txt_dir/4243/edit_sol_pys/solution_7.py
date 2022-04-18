

import sys

def max_happiness(yen):
    """
    Args:
        yen (int): the amount of yen that Takahashi has
    Returns:
        int: the maximum number of happiness points that can be earned
    """
    return yen // 500 * 1000 + yen % 500 // 5 * 5 # ここに処理を書く

def main():
    yen = int(sys.stdin.readline().rstrip())
    print(max_happiness(yen))

if __name__ == '__main__':
    main()

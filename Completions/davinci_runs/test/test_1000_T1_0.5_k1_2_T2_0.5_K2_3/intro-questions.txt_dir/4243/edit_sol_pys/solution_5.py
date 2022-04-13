import sys

def max_happiness(x):
    """
    Args:
        x (int): the amount of yen that Takahashi has
    Returns:
        int: the maximum number of happiness points that can be earned
    """
    return x // 500 * 1000 + (x % 500 // 5) * 5

def main():
    x = int(sys.stdin.readline().rstrip())
    print(max_happiness(x))

if __name__ == '__main__':
    main()

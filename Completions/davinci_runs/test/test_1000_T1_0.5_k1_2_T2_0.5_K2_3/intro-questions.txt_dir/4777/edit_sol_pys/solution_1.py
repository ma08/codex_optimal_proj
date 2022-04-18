

import sys

def main(k):
    x, y = 0, 1
    for _ in range(k):
        x, y = y, x + y
    return x, y

if __name__ == "__main__":
    k = int(sys.stdin.readline())
    x, y = main(k)
    print(x, y)

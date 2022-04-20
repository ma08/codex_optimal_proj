

# SOLUTION

import sys

def get_maximum_play_turns(k, n, a, b):
    if k < a:
        return -1
    elif a == b:
        return n
    elif k == a:
        return n - 1
    elif k == b:
        return n
    else:
        if n == 1:
            return 1
        else:
            return get_maximum_play_turns(k - a, n - 1, a, b) + 1

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        k, n, a, b = map(int, sys.stdin.readline().split())
        print(get_maximum_play_turns(k, n, a, b))

if __name__ == "__main__":
    main()
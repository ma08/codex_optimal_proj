

import math

def main():
    a, b, x = map(int, input().split())
    if x < a + b:
        print(0)
        return

    # Binary search
    left = 0
    right = 10 * 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if a * mid + b * len(str(mid)) <= x:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()

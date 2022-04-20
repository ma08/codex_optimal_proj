
import math

def main():
    a, b, x = map(int, input().split())

    # Binary search
    left = 0
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if a * mid + b * len(str(mid)) > x:
            right = mid
        else:
            left = mid

    print(left)

if __name__ == '__main__':
    main()

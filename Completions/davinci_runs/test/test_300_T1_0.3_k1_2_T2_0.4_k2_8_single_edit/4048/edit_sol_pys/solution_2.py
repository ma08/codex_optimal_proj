
import sys

def main(n):
    if n > 1:
        if n % 2 == 0:
            return main(n // 2) + 1
        else:
            return main(n - 1) + 1
    return 0

if __name__ == '__main__':
    main()

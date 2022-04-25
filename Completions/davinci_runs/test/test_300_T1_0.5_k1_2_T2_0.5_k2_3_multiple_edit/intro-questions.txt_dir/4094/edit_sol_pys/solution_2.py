
import sys

def main():
    k = int(sys.stdin.readline().strip())
    i = 1
    while (7 * (10 ** i) - 7) % k:
        i += 1

if __name__ == '__main__':
    main()

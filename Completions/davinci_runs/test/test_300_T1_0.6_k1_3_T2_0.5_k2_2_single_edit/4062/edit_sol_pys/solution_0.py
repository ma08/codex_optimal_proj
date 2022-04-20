#
#
import sys

def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()]
    min_val = min(a, c)
    max_val = max(b, d)
    print(max_val * max_val)

if __name__ == '__main__':
    main()

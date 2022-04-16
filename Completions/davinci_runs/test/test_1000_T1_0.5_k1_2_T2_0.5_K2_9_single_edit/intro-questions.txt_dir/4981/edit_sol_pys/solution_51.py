
import sys

def main():
    A, B, C = [int(x) for x in sys.stdin.readline().strip().split()]
    order = sys.stdin.readline().strip()
    print("%d %d %d" % (min(A, B, C), max(min(A, B), min(B, C)), max(A, B, C)))

if __name__ == "__main__":
    main()

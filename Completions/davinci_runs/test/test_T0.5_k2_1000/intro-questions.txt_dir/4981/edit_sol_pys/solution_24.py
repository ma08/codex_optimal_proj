
import sys

def main():
    A, B, C = [int(x) for x in sys.stdin.readline().strip().split()]
    order = sys.stdin.readline().strip()
    if order == "ABC":
        print("%d %d %d" % (min(A, B, C), max(min(A, B), min(B, C)), max(A, B, C)))
    elif order == "ACB":
        print("%d %d %d" % (min(A, B, C), max(min(A, C), min(B, C)), max(A, B, C)))
    elif order == "BAC":
        print("%d %d %d" % (min(A, B, C), max(min(A, B), min(A, C)), max(B, C)))
    elif order == "BCA":
        print("%d %d %d" % (min(A, B, C), max(min(B, C), min(A, C)), max(A, B)))
    elif order == "CAB":
        print("%d %d %d" % (min(A, B, C), max(min(A, C), min(B, C)), max(A, B, C)))
    elif order == "CBA":
        print("%d %d %d" % (min(A, B, C), max(min(A, C), min(B, C)), max(A, B, C)))

if __name__ == "__main__":
    main()

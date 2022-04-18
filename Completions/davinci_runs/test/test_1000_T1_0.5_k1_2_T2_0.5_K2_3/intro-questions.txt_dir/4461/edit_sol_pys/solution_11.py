import sys

def main():
    # Get input
    h, w = map(int, sys.stdin.readline().split())
    # If the chocolate bar is a square, the difference between the largest and smallest pieces will be 0
    if h == w:
        print(0)
    else:
        # Otherwise, the difference will be the difference between the larger of the two sides and the smaller of the two sides minus 1.
        print(max(h, w) - min(h, w) - 1)
if __name__ == '__main__':
    main()

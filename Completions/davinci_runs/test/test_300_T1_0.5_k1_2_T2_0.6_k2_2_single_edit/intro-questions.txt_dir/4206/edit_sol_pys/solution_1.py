
import sys

def main():
    # read the input
    s = sys.stdin.readline()
    s = s.strip()
    s = int(s)
    # if the sum is divisible by 3, s is divisible by 3
    if s % 3 == 0:
        print(len(s) - 1)
    else:
        print(0)

    return 0

if __name__ == "__main__":
    main()

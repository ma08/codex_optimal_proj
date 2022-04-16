import sys
import os


def main():
    if len(sys.argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    # TODO

def main():
    s = sys.stdin.readline().rstrip()
    if is_unique(s):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()

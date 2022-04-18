

import sys

def main():
    words = [word for word in sys.stdin.readline().strip().split()]
    if len(words) == len(set(words)):
        print("y")
    else:
        print("n")

if __name__ == "__main__":
    main()

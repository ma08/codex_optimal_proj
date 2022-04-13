

import sys

def main():
    string = sys.stdin.read().splitlines()[0]
    count = string.count('e')
    print("h" + "e" * count + "llo")

if __name__ == "__main__":
    main()

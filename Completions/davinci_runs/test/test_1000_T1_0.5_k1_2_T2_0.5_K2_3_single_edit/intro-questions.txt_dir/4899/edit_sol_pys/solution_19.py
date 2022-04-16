

import sys

def main():
    string = sys.stdin.read().splitlines()[0]
    count = string.count('a')
    print("h" + "a"*count + "y")

if __name__ == "__main__":
    main()

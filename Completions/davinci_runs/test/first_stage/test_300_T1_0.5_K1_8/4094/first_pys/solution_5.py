

import sys

def main():
    k = int(sys.stdin.readline().strip())
    num = 7
    index = 1
    while num % k != 0:
        index += 1
        num = num * 10 + 7
    print(index)

if __name__ == "__main__":
    main()
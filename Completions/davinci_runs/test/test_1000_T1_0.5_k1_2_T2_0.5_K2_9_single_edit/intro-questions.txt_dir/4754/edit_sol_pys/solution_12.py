

import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = [int(x) for x in sys.stdin.readline().strip().split()]
    count = 0

    while socks:
        first = socks.pop()
        try:
            second = socks.pop()
        except:
            print("impossible")
            return

        if first == second:
            count += 1

    print(count)

if __name__ == "__main__":
    main()

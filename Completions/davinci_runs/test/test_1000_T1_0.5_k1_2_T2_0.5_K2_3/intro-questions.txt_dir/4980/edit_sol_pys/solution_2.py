from typing import List

import sys

n = int(sys.stdin.readline())



def main():
    pink_count = 0
    for i in range(n):
        line = sys.stdin.readline()
        if line.lower().find("pink") != -1:
            pink_count += 1

    if pink_count == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(pink_count)


if __name__ == "__main__":
    main()

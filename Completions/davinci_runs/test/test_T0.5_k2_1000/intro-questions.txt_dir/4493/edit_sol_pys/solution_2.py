# A - 台形
# https://atcoder.jp/contests/abc081/tasks/abc081_a

import math
import sys

def main():
    # get input
    s = input()
    # count the number of 1s
    count = 0
    for i in range(len(s)):
        if s[i] == "1":
            count += 1
    print(count)

if __name__ == "__main__":
    main()

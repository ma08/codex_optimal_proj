

import sys

def main():
    num = int(sys.stdin.readline())
    count = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        count += 1
    print(count)

main()
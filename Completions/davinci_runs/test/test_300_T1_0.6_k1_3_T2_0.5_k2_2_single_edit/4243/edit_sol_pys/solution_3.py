

import sys

def main():
    x = int(input())
    happiness = 0
    happiness += (x // 5) * 1000
    x %= 5
    happiness += (x // 5) * 5
    print(happiness)

if __name__ == '__main__':
    main()

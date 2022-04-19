

import sys

def main():
    k = int(input())
    x = 7
    i = 1
    if k == 1:
        print(1)
    else:
        while True:
            if x % k == 0:
                print(i)
                return
            x = x * 10 + 7
            i += 1

if __name__ == '__main__':
    main()

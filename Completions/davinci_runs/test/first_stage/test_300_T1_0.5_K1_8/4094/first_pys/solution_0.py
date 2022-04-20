

import sys

def main():
    k = int(input())
    for i in range(1, 10**6):
        if int("7"*i) % k == 0:
            print(i)
            sys.exit()
    print(-1)

if __name__ == "__main__":
    main()
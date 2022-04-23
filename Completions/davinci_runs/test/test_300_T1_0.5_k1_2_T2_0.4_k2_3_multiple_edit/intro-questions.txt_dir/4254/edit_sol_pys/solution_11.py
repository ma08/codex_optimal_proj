

import sys

def main():
    # sheep, wolves = map(int, sys.stdin.readline().strip().split())
    # if sheep <= wolves:
    #     print("unsafe")
    # else:
    #     print("safe")
    if sys.stdin.readline().strip().split()[0] == '1':
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    main()

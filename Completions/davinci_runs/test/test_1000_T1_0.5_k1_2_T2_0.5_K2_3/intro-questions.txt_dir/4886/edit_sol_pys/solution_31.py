import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    if k <= n:
        print("You will become a flying monkey!!")
    elif k > n:
        print("Your wish is granted!")

if __name__ == '__main__':
    main()

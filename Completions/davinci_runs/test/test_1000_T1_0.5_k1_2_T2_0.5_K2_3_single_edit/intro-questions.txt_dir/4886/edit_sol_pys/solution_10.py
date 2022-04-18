import sys

def main():
    N, K = map(int, sys.stdin.readline().strip().split())
    if K >= N:
        print("Your wish is granted!")
    else:
        print("You will become a flying monkey!")

if __name__ == '__main__':
    main()

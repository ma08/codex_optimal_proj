

import sys

def main():
    n = sys.stdin.readline().strip()

    if int(n) % 25 == 0:
        print(0)
        return

    moves = 0
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            moves += 1
            n = n[:i] + n[i+1:] + n[i]
            if int(n) % 25 == 0:
                print(moves)
                return
    print(-1)

if __name__ == '__main__':
    main()
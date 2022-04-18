#

import sys

def main():
    n = int(sys.stdin.readline())
    pieces = [int(x) for x in sys.stdin.readline().split()]
    pieces.sort()
    player1 = 0
    player2 = 0
    for i in range(n):
        if i % 2 == 0:
            player1 += pieces[n-i-1]
        else:
            player2 += pieces[n-i-1]
    print(player1, player2)

if __name__ == "__main__":
    main()

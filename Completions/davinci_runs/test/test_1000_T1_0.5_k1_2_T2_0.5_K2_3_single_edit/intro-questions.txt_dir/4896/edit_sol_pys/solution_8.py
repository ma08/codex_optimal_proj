

from sys import stdin

def main():
    N = int(stdin.readline())
    bricks = [int(x) for x in stdin.readline().split()]

    towers = 1
    current_height = bricks[0]
    for i in range(1, N):
        if bricks[i] > current_height:
            towers += 1
            current_height = bricks[i]
    print(towers)

if __name__ == '__main__':
    main()

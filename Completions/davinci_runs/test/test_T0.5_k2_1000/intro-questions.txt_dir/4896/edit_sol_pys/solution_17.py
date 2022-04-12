import sys

def main():
    n = int(sys.stdin.readline().strip())
    bricks = list(map(int, sys.stdin.readline().strip().split()))
    towers = [bricks[0]]

    for brick in bricks:
        for i in range(len(towers)):
            if brick < towers[i]:
                towers[i] = brick
                break
            if i == len(towers) - 1:
                towers.append(brick)
                break
    print(len(towers))

if __name__ == '__main__':
    main()

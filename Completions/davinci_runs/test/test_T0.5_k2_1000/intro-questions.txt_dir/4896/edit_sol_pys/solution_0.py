import sys

def main():
    n = int(input())
    bricks = list(map(int, input().split()))
    towers = [bricks[0]]

    for brick in bricks:
        if brick > towers[-1]:  # if new brick is greater than the last brick in the tower
            towers.append(brick)
        else:
            for i in range(len(towers)):
                if brick < towers[i]:  # find the first tower that the new brick is smaller than
                    towers[i] = brick
                    break
    print(len(towers))

if __name__ == '__main__':
    main()

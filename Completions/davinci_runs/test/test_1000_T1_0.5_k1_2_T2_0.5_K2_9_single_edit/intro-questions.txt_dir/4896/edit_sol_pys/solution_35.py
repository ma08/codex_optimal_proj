

def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]
    towers = 0
    base = bricks[0]  # base of the current tower
    for i in range(1, n):  # iterate over the bricks
        if bricks[i] > base:  # if current brick is greater than the base
            towers += 1
            base = bricks[i]  # update the base
    towers += 1
    print(towers)


if __name__ == "__main__":
    main()

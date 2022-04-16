
def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]
    towers = []
    for brick in bricks:
        if len(towers) == 0:
            towers.append(brick)
        else:
            if brick > towers[-1]:
                towers.append(brick)
    print(len(towers))


if __name__ == "__main__":
    main()

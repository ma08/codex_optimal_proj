
def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]  # list comprehension
    towers = []
    for brick in bricks:
        if len(towers) == 0:
            towers.append(brick)
        else:
            if brick > towers[-1]:
                towers.append(brick)
    print(len(towers))


main()

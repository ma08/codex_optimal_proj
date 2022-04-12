
def main():
    n = int(input())  # number of bricks
    bricks = [int(x) for x in input().split()]  # get bricks
    towers = []  # list of towers
    for brick in bricks:  # iterate through bricks
        if len(towers) == 0:  # if no towers
            towers.append(brick)  # add first brick
        else:  # if there are towers
            if brick > towers[-1]:  # if brick is bigger than last brick in tower
                towers.append(brick)  # add brick to tower
    print(len(towers))  # print number of towers


main()



def main():
    n = int(input("Enter number of bricks: "))
    if n > 0:
        bricks = [int(x) for x in input("Enter bricks: ").split()]
        towers = []
        for brick in bricks:
            if len(towers) == 0:
                towers.append(brick)
            else:
                if brick > towers[-1]:
                    towers.append(brick)
        print(len(towers))
    else:
        print("Invalid input")

main()

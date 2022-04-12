

def main():
    """
    Main function
    """
    steel_rods = int(input())  # number of steel rods
    rod_lengths = []  # list of steel rod lengths

    for _ in range(steel_rods):  # get steel rod lengths
        rod_lengths.append(int(input()))

    rod_lengths.sort()
    total_length = 0

    while len(rod_lengths) > 1:
        total_length += rod_lengths[0] + rod_lengths[1] - 1
        rod_lengths.pop(0)
        rod_lengths.pop(0)
        rod_lengths.append(total_length)
        rod_lengths.sort()
        total_length = 0


    print(rod_lengths[0])

if __name__ == "__main__":
    main()



def main():
    """
    Main function
    """
    steel_rods = int(input())  # number of steel rods
    rod_lengths = []  # list of steel rods

    for _ in range(steel_rods):  # input steel rods
        rod_lengths.append(int(input()))

    rod_lengths.sort()  # sort steel rods
    total_length = 0  # total length of steel rods

    while len(rod_lengths) > 1:  # loop until there is only one steel rod left
        total_length += rod_lengths[0] + rod_lengths[1] - 1
        rod_lengths.pop(0)
        rod_lengths.pop(0)
        rod_lengths.append(total_length)
        rod_lengths.sort()
        total_length = 0


    print(rod_lengths[0])

if __name__ == "__main__":
    main()

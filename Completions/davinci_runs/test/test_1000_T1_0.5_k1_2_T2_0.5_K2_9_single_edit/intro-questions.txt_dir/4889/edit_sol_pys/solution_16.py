

def main():
    # read in the number of steel rods.
    num_rods = int(input())

    # read in the lengths of the steel rods.
    rod_lengths = [int(input()) for _ in range(num_rods)]

    # sort the rod lengths in descending order.
    rod_lengths = sorted(rod_lengths, reverse=True)

    # fuse the rods together.
    javelin_length = 0
    for i in range(num_rods - 1):
        javelin_length += rod_lengths[i]
        javelin_length -= 1

    # add the last rod to the javelin.
    javelin_length += rod_lengths[-1]

    # print the length of the javelin
    print(javelin_length)

if __name__ == '__main__':
    main()

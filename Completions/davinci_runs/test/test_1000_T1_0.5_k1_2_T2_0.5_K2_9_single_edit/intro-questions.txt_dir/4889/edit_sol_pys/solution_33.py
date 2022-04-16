

def main():
    # read in the number of steel rods, the length of the javelin, and the number of steel rods to remove
    num_rods, javelin_length, num_to_remove = [int(x) for x in input().split()]

    # read in the lengths of the steel rods
    rod_lengths = [int(input()) for _ in range(num_rods)]

    # sort the rod lengths in descending order
    rod_lengths = sorted(rod_lengths, reverse=True)

    # remove the rods
    for _ in range(num_to_remove):
        javelin_length -= rod_lengths.pop()
        javelin_length -= 1

    # fuse the remaining rods together
    for rod_length in rod_lengths:
        javelin_length += rod_length
        javelin_length -= 1

    # add the last rod to the javelin
    javelin_length += rod_lengths[-1]

    # print the length of the javelin
    print(javelin_length)

if __name__ == '__main__':
    main()

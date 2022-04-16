
def main():
    # read in the number of steel rods and the length of the javelin
    num_rods, javelin_length = map(int, input().split())

    # read in the lengths of the steel rods and sort them in descending order
    rod_lengths = sorted([int(input()) for _ in range(num_rods)], reverse=True)

    # determine the minimum number of rods to be removed
    to_remove = 0
    while javelin_length < sum(rod_lengths):
        javelin_length += rod_lengths[to_remove] - 1
        to_remove += 1

    # print the minimum number of rods to be removed
    print(to_remove)

if __name__ == '__main__':
    main()

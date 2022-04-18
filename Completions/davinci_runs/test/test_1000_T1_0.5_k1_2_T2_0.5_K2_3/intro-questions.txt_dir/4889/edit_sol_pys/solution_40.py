
def main():
    """Main function"""

    steel_rods = int(input())
    rod_lengths = []

    for _ in range(steel_rods):
        rod_lengths.append(int(input()))  # add rod lengths to list

    rod_lengths.sort()  # sort the list
    total_length = 0

    while len(rod_lengths) > 1:
        total_length += rod_lengths[0] + rod_lengths[1] - 1
        rod_lengths.pop(0)  # remove smallest rod length
        rod_lengths.pop(0)  # remove second smallest rod length
        rod_lengths.append(total_length)  # add total length to list
        rod_lengths.sort()  # sort the list
        total_length = 0

    print(rod_lengths[0])  # print the final result

if __name__ == "__main__":
    main()

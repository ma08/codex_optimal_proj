

def main():
    """
    Main function
    """
    file = open("input.txt", "r")
    steel_rods = int(file.readline())
    rod_lengths = [int(line) for line in file]
    rod_lengths.sort()

    total_length = 0

    for i in range(steel_rods - 1):
        total_length += rod_lengths[i] + rod_lengths[i + 1] - 1
        rod_lengths[i + 1] = total_length

    print(total_length)

if __name__ == "__main__":
    main()

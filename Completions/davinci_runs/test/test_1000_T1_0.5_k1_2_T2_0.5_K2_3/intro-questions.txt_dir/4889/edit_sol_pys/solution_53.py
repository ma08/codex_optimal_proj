
def main():
    """
    Main function
    """
    num_of_rods = int(input())
    rod_length = []

    for _ in range(num_of_rods):
        rod_length.append(int(input()))

    rod_length.sort()
    total_length = 0.0

    while len(rod_length) > 1:
        total_length += rod_length[0] + rod_length[1] - 1
        rod_length.pop(0)
        rod_length.pop(0)
        rod_length.append(total_length)
        rod_length.sort()
        total_length = 0

    print(rod_length[0])

if __name__ == "__main__":
    main()

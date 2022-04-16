"""
File
"""

def main():
    """
    Main function
    """
    num_rods = int(input())
    rod_lengths = [int(input()) for _ in range(num_rods)]
    rod_lengths.sort()
    total_length = rod_lengths[0] + rod_lengths[1] - 1
    rod_lengths.pop(0)
    rod_lengths.pop(0)
    rod_lengths.append(total_length)
    rod_lengths.sort()
    total_length = 0

    while len(rod_lengths) > 1: # pylint: disable=C0200
        total_length += rod_lengths[0] + rod_lengths[1] - 1
        rod_lengths.pop(0)
        rod_lengths.pop(0)
        rod_lengths.append(total_length)
        rod_lengths.sort()
        total_length = 0

    print(rod_lengths[0])

if __name__ == "__main__":
    main()

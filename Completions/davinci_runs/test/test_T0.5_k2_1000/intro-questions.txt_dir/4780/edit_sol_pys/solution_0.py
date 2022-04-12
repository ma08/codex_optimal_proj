

def main():
    """
    The main function
    """
    # Read the input
    n1, n2 = [int(x) for x in input().split()]  # pylint: disable=unused-variable
    row1 = list(input())
    row2 = list(input())
    t = int(input())

    # The ants will stay in their original positions if t is even
    if t % 2 == 0:
        print("".join(row1 + row2))
    # Otherwise, the ants will swap places
    else:
        print("".join(row2 + row1))

if __name__ == "__main__":
    main()

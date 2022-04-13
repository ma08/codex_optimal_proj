

def main():
    """
    The main function
    """
    # Read the input
    n1, n2 = [int(x) for x in input().split()]  # read input
    row1 = list(input())
    row2 = list(input())
    t = int(input())  # read input

    # The ants will stay in their original positions if t is even
    if t % 2 == 0:  # check if t is even
        print("".join(row1 + row2))
    # Otherwise, the ants will swap places
    else:
        print("".join(row2 + row1))

if __name__ == "__main__":
    main()

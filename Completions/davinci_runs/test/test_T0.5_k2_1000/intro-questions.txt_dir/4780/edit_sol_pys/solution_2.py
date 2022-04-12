

def main():
    """
    The main function
    """
    # Read the input
    row1 = list(input())
    row2 = list(input())

    # The ants will stay in their original positions if t is even
    print("".join(row1 + row2))
    # Otherwise, the ants will swap places


if __name__ == "__main__":
    main()

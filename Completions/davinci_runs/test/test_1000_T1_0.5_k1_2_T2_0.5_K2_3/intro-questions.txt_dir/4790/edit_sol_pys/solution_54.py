

def main():
    """
    This is the main function that runs the program.

    Returns:
        int: 1 if it is possible to balance the stones with the rules, 0
        otherwise.
    """
    stones = input()
    if len(stones) == 1:
        return 0
    if stones[0] == stones[-1]:
        return 0
    if len(stones) == 2:
        return 1
    return 0


if __name__ == "__main__":
    print(main())



def parse_input():
    """
    Parses input, returns a tuple of integers.
    """
    return tuple(map(int, input().split()))

def main():
    """
    Main function
    """
    a, b, c = parse_input()
    print(min(a, b, c) + min(a, b, c) + min(a, b, c) + min(a, b, c) + min(a, b, c))

if __name__ == "__main__":
    main()
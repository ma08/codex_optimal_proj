

def main():
    """
    Main function
    """
    # Get input
    m, n = map(int, input().split())
    u, l, r, d = map(int, input().split())
    puzzle = []
    for _ in range(m):
        puzzle.append(list(input()))

    print("#" * (n + l + r) + "." * (l + r))
    # Print top margin
    # Print top and bottom
    print("#" * (n + l + r) + "." * (l + r))
    # Print puzzle
    for _ in range(u):
        print("." * (l + r) + "#" * (n + l + r) + "." * (l + r))
    for i in range(m):
        # Print left margin
        print("." * (l + r), end="")
        # Print puzzle
        print("".join(puzzle[i]), end="")
        # Print right margin
        print("." * (l + r))
    # Print bottom margin
    for _ in range(d):
        print("." * (l + r) + "#" * (n + l + r) + "." * (l + r))

if __name__ == "__main__":
    main()

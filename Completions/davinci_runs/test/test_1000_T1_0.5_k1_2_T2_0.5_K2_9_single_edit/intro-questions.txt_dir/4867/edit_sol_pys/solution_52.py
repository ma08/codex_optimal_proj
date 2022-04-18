

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

    # Print top
    print("#" * (n + l + r) + "." * l)
    for _ in range(u):
        print("." * l + "#" * (n + l + r) + "." * l)
    for i in range(m):
        # Print left
        print("." * l, end="")
        # Print puzzle
        print("".join(puzzle[i]), end="")
        # Print right
        print("." * l)
    for _ in range(d):
        print("." * l + "#" * (n + l + r) + "." * l)
    # Print bottom
    print("#" * (n + l + r) + "." * l)

if __name__ == "__main__":
    main()

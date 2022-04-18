

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

    # Print top border
    print("#" * (n + l + r) + "." * (l + r), end="")
    for _ in range(u):
        print("\n" + "." * (l + r) + "#" * (n + l + r) + "." * (l + r), end="")
    for i in range(m):
        # Print left border
        print("\n" + "." * (l + r), end="")
        # Print puzzle
        print("".join(puzzle[i]), end="") 
        # Print right border
        print("." * (l + r), end="")
    for _ in range(d):
        print("\n" + "." * (l + r) + "#" * (n + l + r) + "." * (l + r))
    # Print bottom
    print("\n" + "#" * (n + l + r) + "." * (l + r))

if __name__ == "__main__":
    main()

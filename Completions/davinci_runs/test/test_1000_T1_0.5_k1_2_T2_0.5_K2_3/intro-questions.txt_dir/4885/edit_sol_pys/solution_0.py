

def main():
    """
    Main function
    """

    # Read input.
    white = []
    black = []
    for i in range(8):
        line = input()
        for j in range(8):
            if line[4*j + 1] != ".":
                if line[4*j + 1].isupper():
                    white.append((line[4*j + 1], chr(ord("a") + j) + str(8 - i)))
                else:
                    black.append((line[4*j + 1], chr(ord("a") + j) + str(8 - i)))

    # Sort lists.
    white = sorted(white)
    black = sorted(black, reverse = True)

    # Print output.
    print("White:", ", ".join([x[0] + x[1] for x in white]), sep = "")
    print("Black:", ", ".join([x[0] + x[1] for x in black]), sep = "")

if __name__ == "__main__":
    main()

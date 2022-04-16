

def main():
    """
    Main function
    """

    # read input
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

    # sort lists
    white = sorted(white)
    black = sorted(black, reverse = True)

    # print output
    print("White:", ", ".join([x[0] + x[1] for x in white]))
    print("Black:", ", ".join([x[0] + x[1] for x in black]))

if __name__ == "__main__":
    main()

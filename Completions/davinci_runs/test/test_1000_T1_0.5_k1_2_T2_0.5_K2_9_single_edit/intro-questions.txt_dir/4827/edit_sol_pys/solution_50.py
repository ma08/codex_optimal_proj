

def main():
    # Read the number of words
    N = int(input())

    # Read the words
    words = []
    for i in range(N):
        words.append(input())

    # Find the position of the $
    position = words.index("$")

    # Calculate the number of letters
    number_of_letters = 0
    for i in range(N):
        if i != position:
            number_of_letters += len(words[i])

    # Write the output
    for i in range(N):
        if i == position:
            print(name(number_of_letters), end=" ")
        else:
            print(words[i], end=" ")
    print()


if __name__ == "__main__":
    main()




def main():
    # Get the number of books, n
    n = int(input().strip())

    # Initialize the shelf
    shelf = []

    # Loop over the books
    for i in range(n):
        # Get the book
        book = input().strip().split()

        # If it's a left book
        if book[0] == 'L':  # "L 1"
            # Add it to the left of the shelf
            shelf.insert(0, int(book[1]))

        elif book[0] == 'R':  # "R 1"
            # Add it to the right of the shelf
            shelf.append(int(book[1]))

        # If it's a question
        else:  # "? 1"
            # Find the index of the book
            index = shelf.index(int(book[1]))

            # Print the minimum number of books to pop
            print(min(index, len(shelf) - index - 1))


if __name__ == "__main__":
    main()

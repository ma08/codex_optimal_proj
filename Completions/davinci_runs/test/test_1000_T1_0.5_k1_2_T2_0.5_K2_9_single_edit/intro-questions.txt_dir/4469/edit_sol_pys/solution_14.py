


def main():
    # Get the number of books
    n = int(input())

    # Initialize the shelf
    shelf = []

    # Loop over the books
    for i in range(n):
        # Get the book
        book = int(input())

        # If the book is already on the shelf
        if book in shelf:
            # Find the index of the book
            index = shelf.index(book)

            # Print the minimum number of books to pop
            print(min(index, len(shelf) - index - 1))

        # If the book is not already on the shelf
        else:
            # Add it to the right of the shelf
            shelf.append(book)

            # Print 0
            print(0)


if __name__ == "__main__":
    main()

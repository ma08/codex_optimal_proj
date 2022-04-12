
def main():
    # Get the number of books
    n = int(input())

    # Initialize the books
    books = []

    # Loop over the books
    for i in range(n):
        # Get the book
        book = input().split()

        # If it's a left book
        if book[0] == 'L':
            # Add it to the left of the books
            books.insert(0, int(book[1]))

        # If it's a right book
        elif book[0] == 'R':
            # Add it to the right of the books
            books.append(int(book[1]))

            # Find the index of the book
            index = books.index(int(book[1]))

            # Print the minimum number of books to pop
            print(min(index, len(books) - index - 1))


def main():
    # Get the number of books
    n = int(input())

    # Initialize the books
    books = []

    # Loop over the books
    for i in range(n):
        # Get the book
        book = input().split()

        # If it's a left book
        if book[0] == 'L':
            # Add it to the left of the books
            books.insert(0, int(book[1]))

        # If it's a right book
        elif book[0] == 'R':
            # Add it to the right of the books
            books.append(int(book[1]))

        # If it's a book
        else:
            # Find the index of the book
            index = books.index(int(book[1]))

            # Print the minimum number of books to pop
            print(min(index, len(books) - index - 1))


if __name__ == "__main__":
    main()

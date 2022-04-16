
import sys


def main():
    # Get the number of books
    n = int(input())

    # Initialize the array of books
    books = []

    # Loop over the books
    for i in range(n):
        # Get the book
        book = input()

        # Add it to the array of books
        books.append(book)

    # Print the array of books
    print(books)


if __name__ == "__main__":
    main()

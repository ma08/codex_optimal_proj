
def main():
    # Get the number of books
    n = int(input())

    # Get the books
    books = list(map(int, input().split()))

    # Initialize the number of swaps
    swaps = 0

    # Loop over the books
    for i in range(n):
        # Get the book
        book = books[i]

        # If it's not in the right position
        if book != i + 1:
            # Swap the book with the book in the right position
            books[i], books[book - 1] = books[book - 1], books[i]

            # Increment the number of swaps
            swaps += 1

    # Print the number of swaps
    print(swaps)


if __name__ == "__main__":
    main()

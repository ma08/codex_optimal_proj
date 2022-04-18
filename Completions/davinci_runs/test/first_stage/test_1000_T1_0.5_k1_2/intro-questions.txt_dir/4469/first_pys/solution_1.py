


def main():
    # Get the number of queries
    q = int(input())

    # Initialize the shelf
    shelf = []

    # Loop over the queries
    for i in range(q):
        # Get the query
        query = input().split()

        # If it's a left query
        if query[0] == 'L':
            # Add it to the left of the shelf
            shelf.insert(0, int(query[1]))

        # If it's a right query
        elif query[0] == 'R':
            # Add it to the right of the shelf
            shelf.append(int(query[1]))

        # If it's a question
        else:
            # Find the index of the book
            index = shelf.index(int(query[1]))

            # Print the minimum number of books to pop
            print(min(index, len(shelf) - index - 1))


if __name__ == "__main__":
    main()
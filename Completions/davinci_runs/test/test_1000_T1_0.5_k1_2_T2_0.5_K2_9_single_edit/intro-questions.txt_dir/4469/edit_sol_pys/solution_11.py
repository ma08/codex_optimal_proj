


def main():
    # Get the number of books
    n = int(input())

    # Initialize the stack
    stack = []

    # Loop over the books
    for i in range(n):
        # Get the book
        book = input()

        # If it's the first book
        if i == 0:
            # Add it to the stack
            stack.append(book)

        # If it's not the first book
        else:
            # If it's not the first book and the book is not already in the stack
            if book not in stack:
                # Add it to the stack
                stack.append(book)

    # Print the number of books in the stack
    print(len(stack))


if __name__ == "__main__":
    main()

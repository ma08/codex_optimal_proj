

def main():
    """
    === MAIN ===
    """
    # Get input, k is the number of integers to print, x is the starting number
    input_string = input()
    k = int(input_string.split()[0])
    x = int(input_string.split()[1])

    # Print out all possible x's
    for i in range(1, k):
        print(x - i, end=' ')
    for i in range(k):
        print(x + i, end=' ')

if __name__ == "__main__":
    main()

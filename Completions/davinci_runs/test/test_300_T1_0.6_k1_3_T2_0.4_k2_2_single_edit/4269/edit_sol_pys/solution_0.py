

def main():
    # Read in the number
    n = int(input())
    # Initialize the number of digits
    d = 0
    # Loop through each number from 1 to n
    for i in range(1, n + 1):
        # Check if the number is divisible by 4
        if i % 4 == 0:
            # If so, then increment the number of digits
            d += 1
    # Print the number of digits
    print(d)

if __name__ == '__main__':
    main()



def main():
    # Read in the number
    n = input()
    # Read in the guess
    g = input()
    # Initialize the number of cows and bulls
    cows = 0
    bulls = 0
    # Loop through each digit
    for i in range(4):
        # Check if the digits are the same
        if n[i] == g[i]:
            # If so, increment the number of bulls
            bulls += 1
        else:
            # Check if the digit is in the number
            if g[i] in n:
                # If so, increment the number of cows
                cows += 1
    # Print the results
    print(bulls, "bulls")
    print(cows, "cows")

if __name__ == '__main__':
    main()

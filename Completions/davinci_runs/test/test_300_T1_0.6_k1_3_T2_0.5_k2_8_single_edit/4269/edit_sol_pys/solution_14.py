

def main():
    # Read in the 4-digit number
    s = int(input())
    # Initialize the previous digit
    p = 1
    # Loop through each digit
    for i in range(1, s + 1):
        # Check if the current digit is the same as the previous digit
        if i % 2 == 0:
            # If so, then print Bad and exit
            print("Bad")
            return
        # Otherwise, set the previous digit to the current digit
        p = i + 1
    # If no digit is the same as the previous digit, then print Good
    print("Good")

if __name__ == '__main__':
    main()

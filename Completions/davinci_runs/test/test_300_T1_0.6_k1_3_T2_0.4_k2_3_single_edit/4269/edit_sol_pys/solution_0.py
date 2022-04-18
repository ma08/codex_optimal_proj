

def main():
    # Read in the 4-digit number
    s = int(input())
    # Initialize the previous digit
    p = -1
    # Loop through each digit
    while s > 0:
        # Get the current digit
        i = s % 10
        # Check if the current digit is the same as the previous digit
        if i == p or i == p - 1:
            # If so, then print Bad and exit
            print("Bad")
            return
        # Otherwise, set the previous digit to the current digit
        # Get the next digit
        s = s // 10
        p = i
    # If no digit is the same as the previous digit, then print Good
    print("Good")

if __name__ == '__main__':
    main()

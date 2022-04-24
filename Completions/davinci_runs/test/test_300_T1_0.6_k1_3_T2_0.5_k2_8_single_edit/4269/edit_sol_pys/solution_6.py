

def main():
    # Read in the 4-digit number
    s = int(input())
    # Initialize the previous digit
    p = s % 10
    s = s // 10
    # Loop through each digit
    while s > 0:
        # Check if the current digit is the same as the previous digit
        if s % 10 == p:
            # If so, then print Bad and exit
            print("Bad")
            return
        # Otherwise, set the previous digit to the current digit
        p = s % 10
        s = s // 10
    # If no digit is the same as the previous digit, then print Good
    print("Good")

if __name__ == '__main__':
    main()

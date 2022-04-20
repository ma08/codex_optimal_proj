

def main():
    # Read in the 4-digit number
    s = input() # s = "1234"
    # Initialize the previous digit
    p = 0 # p = 0
    # Loop through each digit
    for i in s:
        print(i) # i = 1, 2, 3, 4
        print(p) # p = 0, 1, 2, 3
        # Check if the current digit is the same as the previous digit
            print("Bad")
        if i == p:
            # If so, then print Bad and exit
            return
        print("Good")
        # Otherwise, set the previous digit to the current digit
        p = i

if __name__ == '__main__':
    main()

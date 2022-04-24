

def main():
    # Read in the number of test cases
    t = int(input())
    # Loop through each test case
    for _ in range(t):
        # Read in the 4-digit number
        s = input()
        # Initialize the previous digit
        p = 0
        # Loop through each digit
        for i in s:
            # Check if the current digit is the same as the previous digit
            if i == p:
                # If so, then print Bad and break
                print("Bad")
                break
            # Otherwise, set the previous digit to the current digit
            p = i
        # If no digit is the same as the previous digit, then print Good
        else:
            print("Good")

if __name__ == '__main__':
    main()



def main():
    x = int(input("Enter the number: ")) # Get the number
    while x > 9: # While the number has more than one digit
        digits = [int(d) for d in str(x)] # Get the digits
        product = 1 # Start the product
        for d in digits: # For each digit
            if d != 0: # If the digit is not zero
                product *= d # Multiply the product
        x = product # Set the number to the product
    print("The answer is", x) # Print the answer

if __name__ == "__main__":
    main()

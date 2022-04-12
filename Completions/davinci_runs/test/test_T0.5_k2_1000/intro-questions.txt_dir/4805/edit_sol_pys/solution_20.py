

def main():
    # Read the input and convert it to an integer
    n = int(input())
    # Create a list to store the numbers
    numbers = []
    # Loop over the numbers
    for i in range(n):
        # Read the number and convert it to an integer
        number = int(input())
        # Add it to the list
        numbers.append(number)
    # Sort the list
    numbers.sort()
    # Print the result
    print(numbers)

if __name__ == "__main__":
    main()

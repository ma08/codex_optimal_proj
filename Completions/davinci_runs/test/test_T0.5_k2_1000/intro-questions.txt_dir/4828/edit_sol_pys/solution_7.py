

def main():
    """
    Main function
    """
    code = input()  # Code to be checked
    nop_count = 0  # Number of NOPs
    for index in range(len(code)):  # Iterate over the code
        if code[index].isupper():  # Check if the current character is an uppercase letter
            if index % 4 != 0:  # Check if the current character is not at the beginning of a line
                nop_count += 4 - (index % 4)  # Add the number of NOPs needed to make the current character at the beginning of a line
    print(nop_count)

if __name__ == "__main__":
    main()

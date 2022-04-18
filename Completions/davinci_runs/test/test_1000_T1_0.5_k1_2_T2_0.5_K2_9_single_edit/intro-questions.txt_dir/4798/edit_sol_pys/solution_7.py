"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""

def main():
    """
    Main function
    """
    input_string = input()
    print("".join([input_string[i] for i in range(len(input_string)) if input_string[i].isupper()]))

if __name__ == "__main__":
    main()

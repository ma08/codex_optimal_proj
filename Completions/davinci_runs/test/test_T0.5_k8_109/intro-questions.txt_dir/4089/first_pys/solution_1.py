

import sys

def main():
    """
    Given an integer N, return the corresponding name for the dog numbered N.
    """
    n = int(sys.stdin.readline().strip())
    if n == 1:
        return "a"

    # Find the number of digits in the name
    digits = 1
    while n > 26**digits:
        n -= 26**digits
        digits += 1

    # Find the number of the letter in the name
    letter = n % 26
    if letter == 0:
        letter = 26
        n -= 26

    # Find the name
    name = ""
    while n > 0:
        name = chr(letter + ord("a") - 1) + name
        n -= letter
        letter = 26
    return name

if __name__ == "__main__":
    print(main())